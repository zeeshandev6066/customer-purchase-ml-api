# 🛒 Customer Purchase Prediction – ML API

A **production-ready Machine Learning REST API** built with **Python, Flask, and Scikit-learn** that predicts whether a customer will make a purchase based on the number of visits.

This project demonstrates **end-to-end ML API development**, including model training, validation, deployment readiness, and clean API responses.

---

## 🚀 Features

- Machine Learning classification model
- Flask REST API
- Input validation & error handling
- Model versioning
- Health check endpoint
- JSON-based predictions
- Ready for deployment

---

## 🧠 Machine Learning Model

- Algorithm: Logistic Regression
- Feature: `customer_visits`
- Target: `purchase` (1 = Yes, 0 = No)

The trained model is saved using `joblib` and loaded directly into the API.

---

## 📂 Project Structure

customer-purchase-ml-api/
│
├── app.py # Flask API
├── customer_purchase_model.pkl # Trained ML model
├── requirements.txt # Dependencies
└── README.md



---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/zeeshandev600/customer-purchase-ml-api.git
cd customer-purchase-ml-api


Install Dependencies
pip install -r requirements.txt

3️⃣ Run the API
python app.py


The API will start at:

http://127.0.0.1:5000


API Endpoints
✅ Health Check
GET /health


Response

{
  "status": "ok",
  "model_version": "1.0.0"
}

🔮 Predict Purchase
POST /predict


Request Body

{
  "customer_visits": 4
}


Response

{
  "model_version": "1.0.0",
  "customer_visits": 4,
  "purchase_prediction": 1,
  "confidence_percent": 78.52
}

❌ Error Handling Examples
Missing Input
{
  "error": "customer_visits is required"
}

Invalid Input
{
  "error": "customer_visits must be a number"
}


Technologies Used

Python

Flask

Scikit-learn

Joblib

NumPy

💼 Use Cases

Customer behavior analysis

Marketing decision support

ML API development demo

Freelance & portfolio project

📈 Future Improvements

Multiple feature support

Authentication

Docker deployment

Cloud hosting (AWS / Render)

Author

Muhammad Zeeshan
Machine Learning & Python Developer

⭐ If you like this project

Give it a ⭐ and feel free to fork!
