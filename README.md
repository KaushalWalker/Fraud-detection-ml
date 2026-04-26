# 🕵️ Fraud Detection ML Project

## Live Application 📺

https://fraud-detection-ml-fb6dcrfsczr7zm8vyfmg7w.streamlit.app

---

## 📌 Overview

This project focuses on detecting fraudulent financial transactions using Machine Learning techniques.

The system analyzes transaction patterns, identifies anomalies, and predicts whether a transaction is fraudulent. The model is deployed using Streamlit for real-time predictions.

---

## 🎯 Problem Statement

Fraudulent transactions are rare but cause significant financial loss. Traditional models struggle due to extreme class imbalance.

The goal is to build a robust model that detects fraud effectively while minimizing false negatives.

---

## 🎯 Objectives

* Analyze transaction data
* Perform Exploratory Data Analysis (EDA)
* Handle imbalanced dataset
* Build ML model
* Deploy using Streamlit

---

## 📊 Exploratory Data Analysis (EDA)

* Checked data types and missing values
* Identified class imbalance
* Visualized fraud vs non-fraud distribution
* Correlation analysis

---

## ⚙️ Data Preprocessing

* Feature selection
* Data cleaning
* Feature scaling (StandardScaler)
* Train-test split with stratification

---

## 🤖 Model Building

**Algorithm:** Gradient Boosting Classifier

**Why:**

* Handles complex patterns
* Works well on structured data

---

## 📈 Model Evaluation

**Primary Metric:** Recall

**Other Metrics:**

* Precision
* F1-score

Focus was on reducing false negatives.

---

## 🚀 Deployment

* Built using Streamlit
* User inputs transaction details
* Model predicts:

  * Fraud / Not Fraud
  * Probability score

---

## 📜 Logging System

* Logs predictions using Python logging module
* Captures:

  * Input data
  * Prediction result
  * Probability score
* Helps in debugging and monitoring

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit
* Joblib

---

## 📂 Project Structure

```
fraud-detection/
│── Fraud_detector.py
│── gr_model.joblib
│── scaler.joblib
│── requirements.txt
│── README.md
```

---

## ⚙️ How to Run

```bash
git clone https://github.com/KaushalWalker/Fraud-detection-ml.git
cd fraud-detection
pip install -r requirements.txt
streamlit run Fraud_detector.py
```

---

## 📁 Dataset

* Transaction-level financial data
* Highly imbalanced
* Not uploaded due to size

---

## 💡 Key Learnings

* Handling imbalanced datasets
* Importance of recall
* ML pipeline development
* Streamlit deployment

---

## 📈 Future Improvements

* Add dashboard visualization
* Use advanced models (XGBoost, LightGBM)
* Cloud deployment (AWS)
* Real-time pipeline

---

## 💼 Business Impact

* 💰 Reduces financial loss
* ⚡ Enables real-time decisions
* 🛡️ Improves fraud detection systems
* 📉 Minimizes risk exposure
* 📊 Provides data insights
