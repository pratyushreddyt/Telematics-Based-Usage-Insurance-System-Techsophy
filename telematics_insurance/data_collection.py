import pandas as pd

def load_telematics_data(filepath):
    df = pd.read_csv(filepath)
    df['speed'] = df['speed'].fillna(0)
    df['acceleration'] = df['acceleration'].fillna(0)
    df['braking_event'] = df['braking_event'].fillna(0)
    df['weather'] = df['weather'].fillna('clear')
    df['time_of_day'] = df['time_of_day'].fillna('unknown')
    if df.isnull().any().any():
        print('Warning: Missing data detected and filled with defaults.')
    return df 