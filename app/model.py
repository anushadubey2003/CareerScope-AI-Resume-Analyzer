import joblib
import pandas as pd

# Load pre-trained resume classifier (trained separately)
model = joblib.load("app/resume_classifier.joblib")

def classify_resume(features):
    df = pd.DataFrame([features])
    return model.predict(df)[0]
