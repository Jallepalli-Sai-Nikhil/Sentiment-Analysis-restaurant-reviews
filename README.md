# 🌟 Sentiment Analysis on Restaurant Reviews

<img src="misc/review_illustration.jpg" width="800" height="350">

#% 📌 Project Overview
This project is a **Sentiment Analysis** system for **restaurant reviews** using **Flask, Sklearn, Joblib, Config.yaml, Docker, and GitHub Actions**. Users can submit their reviews via an HTML UI, and the system will classify them as either **Positive 😊** or **Negative 😞** using a trained machine learning model.

🚀 **Tech Stack:**
- 🧠 **Machine Learning**: Scikit-Learn
- 🏗️ **Web Framework**: Flask + HTML (Jinja2)
- 📦 **Model Storage**: Joblib
- 🔧 **Configuration**: YAML-based settings
- 🐳 **Docker**: Containerized for easy deployment
- ⚙️ **CI/CD**: GitHub Actions (builds & pushes Docker images to Docker Hub)
- ☁️ **Deployment**: Render (Free Tier)

---

## ✨ Features
✔️ **Simple HTML UI** where users enter reviews & get instant sentiment classification  
✔️ **Pre-trained ML model** using Logistic Regression with TF-IDF transformation  
✔️ **Flask Web App** for real-time analysis  
✔️ **GitHub Actions** for CI/CD automation  
✔️ **Docker Image** pushed directly to Docker Hub  
✔️ **Config.yaml-based settings** for flexibility  
✔️ **Secrets Management** via GitHub Secrets for security  
✔️ **Cloud Deployment** on Render (may sleep due to free tier limitations)  
✔️ **Well-structured Codebase** with clear separation of concerns  

---

## 🎬 Local Run Demo Video
[![Watch the Video](https://img.youtube.com/vi/YOUR_VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID_HERE)

## 🎬 Render Deploy Demo Video
[![Watch the Video](https://img.youtube.com/vi/YOUR_VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID_HERE)

## 🎬 DockerHub Demo Video
[![Watch the Video](https://img.youtube.com/vi/YOUR_VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID_HERE)

---

## 💡 Inspiration
In **2023**, during my **internship**, I worked on a **basic sentiment analysis** project using **Kaggle datasets**. However, it was limited to just **model training** and **evaluation**—there was no **Flask app**, no **Dockerization**, no **CI/CD pipelines**, and no **real-world deployment**.

Fast forward to **2025**, I have transformed that simple project into a **full-fledged web application** with modern deployment practices:
- Built a **Flask-based UI** for real-time prediction
- Dockerized the application for easy portability
- Set up **GitHub Actions** for seamless automation
- Hosted it on **Render** for public access
- Integrated **GitHub Secrets** for security

This transformation showcases **how much I've learned** and grown in software engineering, DevOps, and MLOps! 🚀
---

## 🛠️ Setup & Installation
### Prerequisites
- Python 3.12
- Docker
- Git
- GitHub Account with Docker Hub Integration
- 

### 🔹 Clone the Repository
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/sentiment-analysis-flask.git
cd sentiment-analysis-flask
```

### 🔹 Install Dependencies
```bash
pip install --no-cache-dir -r requirements.txt
```

### 🔹 Run Locally
```bash
python app.py
```
Access the app at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🐳 Docker Setup

### 📦 Build and Run with Docker

#### 🔹 1. **Build the Docker Image**
```bash
docker build -t sentiment-analysis .
```
#### 🔹 2. **Run Docker image on local**
```bash
docker run -p 5000:5000 sentiment-analysis
```

### 🔹 Push Docker Image to Docker Hub (via GitHub Actions)
The workflow automatically builds and pushes the image to Docker Hub whenever you push code to the `main` branch.
---

## 🔄 CI/CD with GitHub Actions
🚀 **Automation Pipeline:**
1️⃣ **Push to GitHub** triggers workflow  
2️⃣ **GitHub Actions** builds the Docker image  
3️⃣ **Docker image** is pushed to **Docker Hub**  
4️⃣ **Render** pulls the latest image and deploys it  

📂 **GitHub Secrets Used:**
- `DOCKER_USERNAME` → Your Docker Hub username
- `DOCKER_PASSWORD` → Your Docker Hub password


## 🎨 UI Screenshots
| User Input | Prediction Output |
|------------|------------------|
| ![Input UI](https://source.unsplash.com/300x200/?keyboard,writing) | ![Prediction UI](https://source.unsplash.com/300x200/?emotion,happy) |

---

## 📌 Future Enhancements
### 🚀 Upcoming Features:
✅ Add Deep Learning models (**LSTMs, Transformers**)
✅ Employ Hugging Face API for **LLM models**
✅ **Deploy on AWS/GCP** for scalability
✅ Integrate **MLflow** for model tracking and experiments
✅ Enhance Flask Routes with better logging and error handling
✅ Add many small Python packages **(Flask, Rate Limit, etc.)**
✅ Implement MLOps tools like **DVC, DagsHub**
✅ Use **Google Cloud Storage (GCS)** for dataset & model storage
✅ Integrate **Docker Volumes** for persistent storage on GCP
✅ Utilize **AJAX** & other small frontend libraries for better UX
---

## 👏 Acknowledgments
- **Scikit-Learn** for its simple yet powerful ML tools
- **Flask** for making Python web apps easy
- **Docker** for seamless containerization
- **GitHub Actions** for automated CI/CD
- **Render** for hosting my project for free 🎉

---

## 📜 License
This project is licensed under the **MIT License**.

💙 **If you found this useful, please ⭐ the repo!** 🚀

---

## 📢 Connect With Me
🌐 **Portfolio**: [your-portfolio-link.com](https://your-portfolio-link.com)  
🐦 **Twitter**: [@yourhandle](https://twitter.com/yourhandle)  
📧 **Email**: your-email@example.com  

---

_🔥 Made with ❤️ by [Your Name]_

