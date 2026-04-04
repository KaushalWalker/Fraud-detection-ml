🚀 Fraud Detection ML Project
📌 Overview

This project focuses on detecting fraudulent financial transactions using Machine Learning techniques.

The system analyzes transaction patterns, identifies anomalies, and predicts whether a transaction is fraudulent. The model is deployed using Streamlit for real-time predictions.

🎯 Problem Statement

Fraudulent transactions are rare but cause significant financial loss. Traditional models fail due to high class imbalance, where fraud cases are very few compared to normal transactions.

The goal of this project is to build a robust model that can accurately detect fraud while minimizing false negatives.

🎯 Objectives
Analyze transaction data to understand fraud patterns
Perform detailed Exploratory Data Analysis (EDA)
Handle imbalanced dataset effectively
Build and evaluate Machine Learning models
Deploy the model using Streamlit
📊 Exploratory Data Analysis (EDA)
Checked dataset structure, data types, and missing values
Performed statistical analysis on transaction features
Identified severe class imbalance
Visualized fraud vs non-fraud distribution
Used correlation heatmap to understand feature relationships
⚙️ Data Preprocessing
Feature selection and cleaning
Handling categorical variables
Feature scaling using StandardScaler
Train-test split with stratification to preserve class distribution
🤖 Model Building
Algorithm Used: Gradient Boosting Classifier
Reason:
Handles complex patterns
Performs well on structured data
Sequential learning improves performance
📈 Model Evaluation
Focus Metric: Recall (very important for fraud detection)
Other Metrics:
Precision
F1-score

👉 Priority was given to reducing false negatives (missing fraud cases)

🚀 Deployment
Built an interactive web app using Streamlit
Users can input transaction details
Model predicts:
Fraud / Non-Fraud
Probability score
🛠️ Tech Stack
Python
Pandas, NumPy
Scikit-learn
Streamlit
Joblib
Matplotlib / Seaborn (for EDA)
📂 Project Structure
fraud-detection/
│── Capstone Project-Fraud Detection # jupyter code
│── Fraud_detector.py        # Streamlit app
│── gr_model.joblib          # Trained ML model
│── scaler.joblib            # Feature scaler
│── requirements.txt         # Dependencies
│── README.md                # Documentation
⚙️ How to Run the Project
Clone the repository:
git clone [https://github.com/your-username/fraud-detection.git](https://github.com/KaushalWalker/Fraud-detection-ml/new/main?filename=README.md)
Navigate to project folder:
cd fraud-detection
Install dependencies:
pip install -r requirements.txt
Run the app:
streamlit run Fraud_detector.py
📁 Dataset
Dataset contains transaction-level financial data
Highly imbalanced (fraud cases are very rare)
Not uploaded due to size limitations
💡 Key Learnings
Handling imbalanced datasets in real-world problems
Importance of recall in critical applications
Feature scaling and preprocessing techniques
End-to-end ML pipeline development
Model deployment using Streamlit
📈 Future Improvements
Try advanced models (XGBoost, LightGBM)
Deploy on cloud (AWS / Render)
Improve UI/UX of dashboard
Real-time fraud detection pipeline


💼 Business Impact
💰 Reduces Financial Loss: Early fraud detection prevents monetary damage
⚡ Real-Time Decision Making: Instant predictions help in blocking suspicious transactions
🛡️ Improves Security Systems: Strengthens fraud monitoring frameworks
📉 Minimizes Risk Exposure: Focus on recall ensures fewer fraud cases are missed
📊 Data-Driven Insights: Helps organizations understand fraud patterns and take preventive actions
🙋‍♂️ Author

Kaushal Jambhle
AI/ML Engineer
