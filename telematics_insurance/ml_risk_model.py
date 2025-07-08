import pandas as pd
from sklearn.linear_model import LogisticRegression
import numpy as np

FEATURES = ['speed', 'acceleration', 'braking_event']

def simulate_labels(df):
    return ((df['event_type'].isin(['speeding', 'harsh_braking'])) | (df.get('weather', '') == 'rainy')).astype(int)

def train_model(df):
    X = df[FEATURES]
    y = simulate_labels(df)
    model = LogisticRegression()
    model.fit(X, y)
    return model

def predict_risk(model, df):
    X = df[FEATURES]
    risk_probs = model.predict_proba(X)[:,1]
    df['ml_risk_score'] = (risk_probs > 0.5).astype(int) * 3
    total_risk = df['ml_risk_score'].sum()
    return df, total_risk 