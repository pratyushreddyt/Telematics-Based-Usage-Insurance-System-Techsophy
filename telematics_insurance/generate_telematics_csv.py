import csv
import random
from datetime import datetime, timedelta

# Settings
N_ROWS = 500
START_TIME = datetime(2024, 7, 8, 8, 0, 0)
LAT, LON = 12.9716, 77.5946

weather_options = ['clear', 'rainy']
time_of_day_options = ['morning', 'afternoon', 'evening', 'night']
event_types = ['normal', 'speeding', 'harsh_braking']

with open('telematics_insurance/data/sample_telematics_xlarge.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['timestamp','speed','acceleration','braking_event','latitude','longitude','event_type','weather','time_of_day'])
    time = START_TIME
    lat, lon = LAT, LON
    for i in range(N_ROWS):
        # Simulate time
        time += timedelta(seconds=random.randint(1, 5))
        # Simulate location
        lat += random.uniform(-0.0005, 0.0005)
        lon += random.uniform(-0.0005, 0.0005)
        # Simulate weather and time of day
        weather = random.choices(weather_options, weights=[0.8, 0.2])[0]
        tod = time_of_day_options[(time.hour // 6) % 4]
        # Simulate event
        event = random.choices(event_types, weights=[0.7, 0.2, 0.1])[0]
        if event == 'normal':
            speed = random.randint(35, 55)
            acceleration = round(random.uniform(-0.5, 0.5), 2)
            braking_event = 0
        elif event == 'speeding':
            speed = random.randint(56, 80)
            acceleration = round(random.uniform(0.3, 1.5), 2)
            braking_event = 0
        else:  # harsh_braking
            speed = random.randint(30, 65)
            acceleration = round(random.uniform(-2.5, -1.0), 2)
            braking_event = 1
        writer.writerow([
            time.strftime('%Y-%m-%d %H:%M:%S'),
            speed,
            acceleration,
            braking_event,
            round(lat, 6),
            round(lon, 6),
            event,
            weather,
            tod
        ])
print('Generated 500 rows in data/sample_telematics_xlarge.csv') 