import streamlit as st
import pandas as pd
import os
from data_collection import load_telematics_data
from behavior_analysis import analyze_behavior
from risk_scoring import score_risk
from ml_risk_model import train_model, predict_risk
from pricing import adjust_premium
from feedback import generate_feedback

st.set_page_config(page_title="Telematics Insurance Dashboard", layout="wide")
st.title("Telematics-Based Usage Insurance Dashboard")

def get_data():
    uploaded = st.file_uploader("Upload telematics CSV", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
    else:
        sample_path = os.path.join(os.path.dirname(__file__), 'data', 'sample_telematics.csv')
        df = load_telematics_data(sample_path)
    return df

df = get_data()
mode = st.radio("Select Risk Scoring Mode", ["Rule-based", "ML-based"])
df = analyze_behavior(df)
if mode == "ML-based":
    model = train_model(df)
    df, total_risk = predict_risk(model, df)
    risk_col = 'ml_risk_score'
else:
    df, total_risk = score_risk(df)
    risk_col = 'risk_score'
premium = adjust_premium(total_risk)
feedback = generate_feedback(df)
st.subheader("Summary")
st.metric("Total Risk Score", total_risk)
st.metric("Adjusted Premium", f"${premium}")
st.write("**Safety Recommendations:**")
for rec in feedback:
    st.write(f"- {rec}")
st.subheader("Driving Data Visualization")
st.line_chart(df['speed'], use_container_width=True)
st.bar_chart(df['detected_event'].value_counts())
if 'latitude' in df.columns and 'longitude' in df.columns:
    st.subheader("Route Map")
    st.map(df.rename(columns={'latitude':'lat','longitude':'lon'})) 