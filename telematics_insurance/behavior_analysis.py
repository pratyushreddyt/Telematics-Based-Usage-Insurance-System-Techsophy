def analyze_behavior(df):
    def detect_event(row):
        if row['braking_event'] == 1 or row['acceleration'] < -1.0:
            return 'harsh_braking'
        elif row['speed'] > 50:
            if row['weather'] == 'rainy':
                return 'speeding_rain'
            return 'speeding'
        else:
            return 'normal'
    df['detected_event'] = df.apply(detect_event, axis=1)
    return df 