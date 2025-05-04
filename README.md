# Reddit Sentiment Dashboard

This project is a web application that fetches trending Reddit posts from a user-specified subreddit, performs sentiment analysis on the post titles and comments using VADER, and visualizes the results. It is built using Flask and MongoDB and is deployed on Microsoft Azure.

---

## 🧑‍💻 Team Members

1. Yash Takte
2. Sejal Nimkar
3. Niranjan Tapasvi

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
## 📸 Section 5: Screenshots

### 🏠 Landing Page (Home Page)  
Landing page that welcomes users to the sentiment analysis tool.<br>  
<img width="1705" alt="image" src="https://github.com/user-attachments/assets/3e5b8eb3-8630-4e4e-80e0-b479a3ca1dac" />

---

### 📋 Dashboard  
For demonstration purposes, the subreddit **LLM** was used.<br>  
Users can add, edit, or delete posts manually.<br>  
![Dashboard](<img width="1703" alt="image" src="https://github.com/user-attachments/assets/c87e3c9a-d8b1-41dc-b9ef-35836139bf39" />)

---

### 📊 Visualizations  

**Bar Chart – Sentiment Distribution**<br>  
Shows the count of posts classified as Positive, Neutral, or Negative.<br>  
![Sentiment Distribution](<img width="1459" alt="image" src="https://github.com/user-attachments/assets/614bcca9-130f-4d7e-89df-d7bc16e462dd" />)

**Line Chart – Sentiment Trend Over Time**<br>  
Displays how the average sentiment score changes daily.<br>  
![Sentiment Trend](<img width="1366" alt="image" src="https://github.com/user-attachments/assets/562c300b-a6c5-4c57-b864-3d02658972f3" />)

**Bar Chart – Most Discussed Keywords**<br>  
Highlights the most frequent keywords in analyzed Reddit post titles.<br>  
![Keywords](<img width="1489" alt="image" src="https://github.com/user-attachments/assets/e2dc487f-1942-414b-a3f1-85edebb521d7" />)


---

## 🌐 Hosted App

🔗 [Visit the Deployed Dashboard Here](https://adtproject-h2bjg0d7aaezg4af.eastus-01.azurewebsites.net/dashboard) 
