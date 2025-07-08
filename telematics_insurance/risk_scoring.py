def score_risk(df):
    def event_score(event):
        if event == 'speeding_rain':
            return 4
        elif event == 'harsh_braking':
            return 3
        elif event == 'speeding':
            return 2
        else:
            return 0
    df['risk_score'] = df['detected_event'].apply(event_score)
    total_risk = df['risk_score'].sum()
    return df, total_risk 