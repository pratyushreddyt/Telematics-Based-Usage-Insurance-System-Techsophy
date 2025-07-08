import os
import time
import pandas as pd
from data_collection import load_telematics_data
from behavior_analysis import analyze_behavior
from risk_scoring import score_risk
from pricing import adjust_premium
from feedback import generate_feedback
from ml_risk_model import train_model, predict_risk

DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'sample_telematics.csv')
STREAMING = True
STREAM_DELAY = 0.5
ML_MODE = True

def main():
    df = load_telematics_data(DATA_PATH)
    if ML_MODE:
        model = train_model(df)
    if STREAMING:
        print('--- Streaming Usage-Based Insurance Report ---')
        running_df = df.iloc[0:0].copy()
        for idx, row in df.iterrows():
            running_df = pd.concat([running_df, pd.DataFrame([row])], ignore_index=True)
            running_df = analyze_behavior(running_df)
            if ML_MODE:
                running_df, total_risk = predict_risk(model, running_df)
            else:
                running_df, total_risk = score_risk(running_df)
            premium = adjust_premium(total_risk)
            feedback = generate_feedback(running_df)
            print(f'\n[Data Point {idx+1}] Timestamp: {row["timestamp"]}')
            print(f'Current Risk Score: {total_risk} | Premium: ${premium}')
            print('Feedback:')
            for rec in feedback:
                print(f'- {rec}')
            time.sleep(STREAM_DELAY)
    else:
        df = analyze_behavior(df)
        if ML_MODE:
            df, total_risk = predict_risk(model, df)
        else:
            df, total_risk = score_risk(df)
        premium = adjust_premium(total_risk)
        feedback = generate_feedback(df)
        print('--- Usage-Based Insurance Report ---')
        print(f'Total Risk Score: {total_risk}')
        print(f'Adjusted Premium: ${premium}')
        print('Safety Recommendations:')
        for rec in feedback:
            print(f'- {rec}')

if __name__ == '__main__':
    main() 