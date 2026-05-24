# 🩸 Blood Cancer Detection System using CNN (EfficientNet)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Django](https://img.shields.io/badge/Django-5.1-green)
![TensorFlow](https://img.shields.io/badge/TensorFlow-DeepLearning-orange)
![License](https://img.shields.io/badge/License-Academic-red)

AI-powered Blood Cancer Detection Web Application using Deep Learning, Computer Vision, Django REST Framework, and TensorFlow.

---

# 🚀 Features

- 🔬 Blood Cancer Detection from Blood Cell Images
- 🧠 CNN / EfficientNet Deep Learning Model
- 🌐 Full Stack Django Web Application
- 📤 Image Upload Functionality
- 📊 Prediction Confidence Score
- ⚡ REST API Integration
- 📱 Responsive Frontend UI
- 🖼️ Real-Time Prediction Display

---

# 📌 Project Objective

Traditional blood cancer diagnosis depends on manual microscopic analysis by pathologists, which is:

- Time-consuming
- Expensive
- Error-prone

This project automates the diagnosis process using Deep Learning and Computer Vision techniques to:

- Improve diagnosis speed
- Increase prediction accuracy
- Reduce human dependency
- Assist healthcare professionals

---

# 🏗️ System Architecture

```text
User Uploads Blood Cell Image
            │
            ▼
Frontend (HTML/CSS/JS)
            │
            ▼
Django REST API
            │
            ▼
Image Preprocessing
(OpenCV + NumPy)
            │
            ▼
CNN / EfficientNet Model
            │
            ▼
Prediction Generation
            │
            ▼
Frontend Displays Result
```

---

# 🧠 Deep Learning Models Used

| Model | Purpose |
|------|------|
| CNN | Feature Extraction |
| EfficientNetB0 | Lightweight High Accuracy Model |

---

# 🛠️ Tech Stack

## Backend

- Django
- Django REST Framework

## Machine Learning

- TensorFlow
- Keras
- CNN
- EfficientNetB0

## Frontend

- HTML5
- CSS3
- JavaScript

## Image Processing

- OpenCV
- NumPy
- Pillow

## Data Visualization

- Matplotlib
- Seaborn

## Database

- SQLite3

---

# 📂 Project Structure

```text
BloodDetect_Project/
│
├── backend/
├── frontend/
├── model/
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation Guide

## Clone Repository

```bash
git clone https://github.com/ankith179/Blood-Cancer-Detection-.git
```

## Create Virtual Environment

```bash
python -m venv .venv
```

## Activate Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Project

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

# 🌐 Server URL

```text
http://127.0.0.1:8000/
```

---

# 🔌 API Endpoint

## Prediction API

```http
POST /api/predict/
```

---

# 📥 Response Example

```json
{
    "Prediction": "Cancerous",
    "Confidence": "97.25%"
}
```

---

# 📊 Performance Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

# 🚀 Deployment Platforms

- Render
- Railway
- Vercel
- Docker
- AWS EC2

---

# 👨‍💻 Authors

- Ankith Singh

---

# 📄 License

This project is developed for academic and research purposes only.
