import joblib
import pandas as pd

joblib.parallel_backend('threading', n_jobs=1)
def predict(data):    
    model = joblib.load('artifacts/model_classification.pkl')
    try:
        df = pd.DataFrame([data])
    except:
        df = data
    prediction = model.predict(df)
    probability = model.predict_proba(df)
    return {'prediction': int(prediction[0]), 'probability': float(probability[0][1])}