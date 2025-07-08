# 🚗 Telematics-Based Usage Insurance System

Hi there! 👋
Welcome to my project for usage-based insurance—a real-world, data-driven solution that brings together AI, analytics, and user experience. This system analyzes driving behavior to offer fair, dynamic insurance pricing and personalized safety feedback.

---

## 🌟 Why I Built This
Insurance shouldn’t be one-size-fits-all. With telematics, we can reward safe drivers, encourage better habits, and make roads safer for everyone. I wanted to show how AI and data engineering can make a real impact—while building something modular, scalable, and easy to use.

---

## 🧩 What’s Inside
- **Behavior Analysis:** Detects risky events like speeding and harsh braking, and even considers weather conditions.
- **Risk Scoring:** Both rule-based and machine learning (logistic regression) models.
- **Dynamic Premiums:** Insurance costs that actually reflect how you drive.
- **Personalized Feedback:** Actionable tips to help drivers stay safe and save money.
- **Interactive Dashboard:** Upload your own data, see instant results, and explore visualizations.
- **Handles Real-World Data:** Works with missing/corrupt data, large files, and streaming or batch inputs.

---

## 🏗️ How It Works
```
Telematics Data (CSV/Stream)
        ↓
[Data Collection] → [Behavior Analysis] → [Risk Scoring (Rule/ML)] → [Pricing] → [Feedback]
```

---

## 🚀 Try It Yourself
1. **Clone the Repo**
   ```bash
   git clone https://github.com/yourusername/telematics-insurance-system.git
   cd telematics-insurance-system
   ```
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Launch the Dashboard**
   ```bash
   python -m streamlit run telematics_insurance/dashboard.py
   ```
   (Open http://localhost:8501 in your browser)
4. **Test the Pipeline**
   ```bash
   python telematics_insurance/test_pipeline.py
   ```

---

## 📂 Data Format
You can use the provided sample files or upload your own.
**Required columns:**
- `timestamp`, `speed`, `acceleration`, `braking_event`, `latitude`, `longitude`, `event_type`, `weather`, `time_of_day`

Example:
```csv
timestamp,speed,acceleration,braking_event,latitude,longitude,event_type,weather,time_of_day
2024-07-08 08:00:00,45,0.2,0,12.9716,77.5946,normal,clear,morning
```

---

## 🛠️ Project Structure
- `data_collection.py` – Loads and cleans data
- `behavior_analysis.py` – Detects risky driving
- `risk_scoring.py` – Rule-based scoring
- `ml_risk_model.py` – ML-based scoring
- `pricing.py` – Premium calculation
- `feedback.py` – Safety recommendations
- `main.py` – Main pipeline
- `dashboard.py` – Streamlit dashboard
- `test_pipeline.py` – Test script
- `generate_telematics_csv.py` – Generate large synthetic datasets

---

## 🔒 Privacy Disclaimer
This project uses only synthetic or user-supplied data. In a real deployment, all telematics data should be handled in compliance with privacy laws and best practices. No personal data is collected or stored by this code.

---

## 🙋‍♂️ About Me
I’m passionate about building real-world, data-driven solutions that bridge the gap between AI and business value. Let’s connect! 