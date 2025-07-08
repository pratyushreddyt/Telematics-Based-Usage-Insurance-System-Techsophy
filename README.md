# Telematics-Based Usage Insurance System – Techsophy

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-red)](https://streamlit.io/)

This project is a smart, usage-based insurance system that analyzes real driving behavior to offer fair, dynamic insurance pricing and personalized safety recommendations. It uses telematics data such as speed, acceleration, braking, and contextual information (like weather and time of day) to identify risky patterns, compute a risk score, and adjust premiums accordingly.

---

## Table of Contents

- [Features](#features)
- [Project Highlights](#project-highlights)
- [Modules Overview](#modules-overview)
- [Input Data Format](#input-data-format)
- [Output Screenshots](#output-screenshots)
- [Author](#author)

---

## Features

- Detects unsafe driving behaviors (e.g., harsh braking, speeding)
- Calculates risk scores using both rule-based logic and machine learning models
- Dynamically adjusts insurance premiums based on driving risk
- Provides personalized safety tips to drivers
- Includes an interactive dashboard for data upload and analysis
- Designed with a modular and scalable architecture

---

## Project Highlights

- Behavioral event detection: speeding, harsh braking, and rapid acceleration
- Dual-mode risk scoring: rule-based logic and ML-driven prediction
- Premium adjustment engine based on risk profiles
- Personalized driving feedback generation
- Streamlit dashboard for visual analytics and data interaction
- End-to-end modular pipeline for clarity and maintainability

---

## Modules Overview

- `data_collection.py`: Handles data ingestion, validation, and cleaning  
- `behavior_analysis.py`: Detects driving events like harsh braking or speeding  
- `risk_scoring.py`: Computes risk scores using predefined rules  
- `ml_risk_model.py`: Applies machine learning to score driver risk  
- `pricing.py`: Adjusts insurance pricing based on computed risk  
- `feedback.py`: Generates actionable safety feedback for the driver  
- `dashboard.py`: Web-based UI using Streamlit for interaction and insights  
- `test_pipeline.py`: Complete simulation and flow tester  
- `generate_telematics_csv.py`: Utility to create synthetic datasets  

---

## Input Data Format

You can upload a CSV file or use the samples provided. The dataset must include the following fields:

| Field         | Description                                   |
|---------------|-----------------------------------------------|
| timestamp     | Timestamp of the recorded event               |
| speed         | Vehicle speed in kilometers per hour (km/h)   |
| acceleration  | Measured acceleration (m/s²)                  |
| braking_event | 1 if a harsh braking event occurred, else 0   |
| latitude      | GPS latitude of the vehicle                   |
| longitude     | GPS longitude of the vehicle                  |
| event_type    | Event category (e.g., normal, braking, speeding) |
| weather       | Environmental conditions (e.g., clear, rain)  |
| time_of_day   | Part of the day (morning, afternoon, night)   |

**Sample Data:**

```csv
timestamp,speed,acceleration,braking_event,latitude,longitude,event_type,weather,time_of_day
2024-07-08 08:00:00,45,0.2,0,12.9716,77.5946,normal,clear,morning
