# Reddit Sentiment Dashboard

This project is a web application that fetches trending Reddit posts from a user-specified subreddit, performs sentiment analysis on the post titles and comments using VADER, and visualizes the results. It is built using Flask and MongoDB and is deployed on Microsoft Azure.

---

## 🔧 Features

- Fetches top Reddit posts from a specified subreddit using the Reddit API.
- Performs sentiment analysis using the VADER SentimentIntensityAnalyzer.
- Stores analyzed data in a MongoDB Atlas database.
- Displays an interactive dashboard with:
  - Sentiment distribution
  - Sentiment trend over time
  - Most discussed keywords
- Supports manual CRUD operations:
  - Add, edit, and delete posts through the dashboard.
- Provides REST APIs for external consumption.

---

## 📊 API Endpoints

- `GET /api/sentiment_distribution`: Returns counts of each sentiment category.
- `GET /api/sentiment_trend`: Returns average sentiment score over time.
- `GET /api/most_discussed_keywords`: Returns top 10 frequent words from post titles.
- `GET /api/total_posts`: Returns total number of stored posts.

---

## 🛠️ Technologies Used

- **Frontend**: HTML, CSS, Javascript, Bootstrap
- **Backend**: Flask (Python)
- **Database**: MongoDB Atlas
- **APIs**: Reddit API via `praw`
- **Sentiment Analysis**: `vaderSentiment`
- **Deployment**: Microsoft Azure App Service (Linux, Python 3.10)

---

## 🌐 Hosted App

🔗 [Visit the Deployed Dashboard Here](https://adtproject-h2bjg0d7aaezg4af.eastus-01.azurewebsites.net/) 
