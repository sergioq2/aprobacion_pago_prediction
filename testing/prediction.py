import joblib
import pandas as pd
import os

def predict(data):
    base_path = os.path.dirname(__file__)
    model_path = os.path.join(base_path, 'model_classification.pkl')
    model = joblib.load(model_path)
    try:
        df = pd.DataFrame([data])
    except:
        df = data
    prediction = model.predict(df)
    probability = model.predict_proba(df)
    return {'prediction': int(prediction[0]), 'probability': float(probability[0][1])}
