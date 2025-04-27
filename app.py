from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from pymongo import MongoClient
from bson.objectid import ObjectId
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import praw
import datetime
import os
import uuid

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Enable sessions

# MongoDB connection
client = MongoClient("mongodb+srv://sejnimka:root1234@cluster0.9ke9pe9.mongodb.net/?retryWrites=true&w=majority&tls=true")
db = client["reddit_db"]
collection = db["reddit_posts"]

# Reddit API setup
reddit = praw.Reddit(
    client_id="ZYSmqByC2Mhh22QXzYp9Sw",
    client_secret="6NQTzuEGjYgIcgedUi2bqefpGIERuQ",
    user_agent="adt_app by /u/Longjumping_Cod9778"
)

analyzer = SentimentIntensityAnalyzer()

@app.route("/")
def home():
    return render_template("intro.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())  # Assign session ID to user

    posts = []  # Default: empty posts

    if request.method == "POST":
        subreddit_name = request.form["subreddit"]
        subreddit = reddit.subreddit(subreddit_name)

        inserted_count = 0

        for post in subreddit.hot(limit=15):
            if post.num_comments < 3:
                continue

            post.comments.replace_more(limit=None)
            top_comments = post.comments.list()[:200]
            comment_text = " ".join([comment.body for comment in top_comments])
            combined_text = post.title + " " + comment_text

            score = analyzer.polarity_scores(combined_text)
            label = (
                "Positive" if score["compound"] > 0.05
                else "Negative" if score["compound"] < -0.05
                else "Neutral"
            )

            collection.insert_one({
                "title": post.title,
                "score": post.score,
                "comments": post.num_comments,
                "created": datetime.datetime.fromtimestamp(post.created_utc),
                "comment_text": comment_text,
                "sentiment": label,
                "sentiment_score": score["compound"],
                "session_id": session['session_id']  # ⭐ Save user's session ID
            })

            inserted_count += 1

        print(f"Inserted {inserted_count} new records.")

    # Fetch only posts belonging to this session
    posts = list(collection.find({"session_id": session['session_id']}))
    return render_template("index.html", posts=posts, total_posts=len(posts))

@app.route("/create", methods=["POST"])
def create():
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())

    title = request.form["title"]
    score = int(request.form["score"])
    comments = int(request.form["comments"])
    sentiment = request.form["sentiment"]
    sentiment_score = 1 if sentiment == "Positive" else -1 if sentiment == "Negative" else 0

    collection.insert_one({
        "title": title,
        "score": score,
        "comments": comments,
        "created": datetime.datetime.now(),
        "comment_text": "",
        "sentiment": sentiment,
        "sentiment_score": sentiment_score,
        "session_id": session['session_id']
    })
    return redirect(url_for("dashboard"))

@app.route("/delete/<post_id>")
def delete(post_id):
    collection.delete_one({"_id": ObjectId(post_id)})
    return redirect(url_for("dashboard"))

@app.route("/update/<post_id>", methods=["POST"])
def update_post(post_id):
    title = request.form["title"]
    score = int(request.form["score"])
    comments = int(request.form["comments"])
    sentiment = request.form["sentiment"]

    collection.update_one(
        {"_id": ObjectId(post_id)},
        {"$set": {
            "title": title,
            "score": score,
            "comments": comments,
            "sentiment": sentiment
        }}
    )
    return redirect(url_for("dashboard"))

@app.route("/api/sentiment_distribution")
def sentiment_distribution():
    sentiments = {"Positive": 0, "Neutral": 0, "Negative": 0}
    for post in collection.find({"session_id": session.get('session_id', '')}):
        sentiments[post["sentiment"]] += 1
    return jsonify(sentiments)

@app.route("/api/sentiment_trend")
def sentiment_trend():
    trend = collection.aggregate([
        {"$match": {"session_id": session.get('session_id', '')}},
        {"$group": {
            "_id": {"$dateToString": {"format": "%Y-%m-%d", "date": "$created"}},
            "average": {"$avg": "$sentiment_score"}
        }},
        {"$sort": {"_id": 1}}
    ])
    return jsonify(list(trend))

@app.route("/api/most_discussed_keywords")
def most_discussed_keywords():
    pipeline = [
        {"$match": {"session_id": session.get('session_id', '')}},
        {"$project": {"title": {"$toLower": "$title"}}},
        {"$project": {"words": {"$split": ["$title", " "]}}},
        {"$unwind": "$words"},
        {"$match": {"words": {"$nin": ["the", "is", "and", "of", "to", "a", "in", "for", "on", "with", "that"]}}},
        {"$group": {"_id": "$words", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    result = list(collection.aggregate(pipeline))
    return jsonify(result)

@app.route("/api/total_posts")
def get_total_posts():
    total = collection.count_documents({"session_id": session.get('session_id', '')})
    return jsonify({"total": total})

@app.route("/visualize")
def visualize():
    return render_template("visualize.html")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

