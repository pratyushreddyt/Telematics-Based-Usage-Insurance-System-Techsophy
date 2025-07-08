import os
from data_collection import load_telematics_data
from behavior_analysis import analyze_behavior
from risk_scoring import score_risk
from ml_risk_model import train_model, predict_risk
from pricing import adjust_premium
from feedback import generate_feedback

DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'sample_telematics.csv')

def test_rule_based():
    df = load_telematics_data(DATA_PATH)
    df = analyze_behavior(df)
    df, total_risk = score_risk(df)
    premium = adjust_premium(total_risk)
    feedback = generate_feedback(df)
    print('Rule-based risk score:', total_risk)
    print('Rule-based premium:', premium)
    print('Rule-based feedback:', feedback)

def test_ml_based():
    df = load_telematics_data(DATA_PATH)
    df = analyze_behavior(df)
    model = train_model(df)
    df, total_risk = predict_risk(model, df)
    premium = adjust_premium(total_risk)
    feedback = generate_feedback(df)
    print('ML-based risk score:', total_risk)
    print('ML-based premium:', premium)
    print('ML-based feedback:', feedback)

if __name__ == '__main__':
    print('--- Testing Rule-Based Pipeline ---')
    test_rule_based()
    print('\n--- Testing ML-Based Pipeline ---')
    test_ml_based() 