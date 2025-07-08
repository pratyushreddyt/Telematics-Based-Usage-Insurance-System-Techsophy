def generate_feedback(df):
    feedback = []
    if (df['detected_event'] == 'harsh_braking').any():
        feedback.append('Avoid harsh braking to reduce accident risk.')
    if (df['detected_event'] == 'speeding_rain').any():
        feedback.append('Never speed in rainy weather; risk of accident is much higher.')
    if (df['detected_event'] == 'speeding').any():
        feedback.append('Reduce speeding to improve safety and lower premiums.')
    if not feedback:
        feedback.append('Good driving! Keep it up.')
    return feedback 