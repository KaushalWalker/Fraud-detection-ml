import streamlit as st
import pandas as pd
import joblib 

# Load model and scaler 
model = joblib.load("gr_model.joblib")
scaler = joblib.load("scaler.joblib")

# Title
st.title("💻 Fraud Detection App")
st.write("Enter Transaction details to check if it's Fraud or Not")

# Sidebar
st.sidebar.title("About")
st.sidebar.write("Detect Fraudulent transaction using ML")

# Input Fields
step = st.number_input("Step (Time of Transactions)", min_value=0)
amount = st.number_input("Transaction Amount", min_value=0.0)
oldbalanceOrg = st.number_input("Old Balance(Sender)", min_value=0.0)
newbalanceOrig = st.number_input("New Balance(Sender)", min_value=0.0)
oldbalanceDest = st.number_input("Old Balance(Receiver)", min_value=0.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0)

type_option = st.selectbox(
    "Transaction Type",
    ["TRANSFER", "CASH_OUT", "PAYMENT", "DEBIT", "CASH_IN"]
)

# Predict
if st.button("Predict"):

    # Feature Engineering
    balance_diff_org = oldbalanceOrg - newbalanceOrig
    balance_diff_dest = newbalanceDest - oldbalanceDest

    # One-hot encoding
    input_data = {
        "step": step,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest,
        "balance_diff_org": balance_diff_org,
        "balance_diff_dest": balance_diff_dest,
        "type_CASH_IN": 0,
        "type_CASH_OUT": 0,
        "type_DEBIT": 0,
        "type_PAYMENT": 0,
        "type_TRANSFER": 0
    }

    input_data[f"type_{type_option}"] = 1

    # Convert to DataFrame
    df = pd.DataFrame([input_data])

    # Scale
    df_scaled = scaler.transform(df)

    # Prediction + Probability
    prob = model.predict_proba(df_scaled)[0][1]

    # Output
    if prob > 0.5:
        st.error(f"🚨 Fraud Detected! (Probability: {prob:.2f})")
    else:
        st.success(f"✅ Safe Transaction (Fraud Probability: {prob:.2f})")