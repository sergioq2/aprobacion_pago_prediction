import pandas as pd
from preprocessing import clean_data
from prediction import predict

def handler(event, context):
    try:
        body = event['body']
    except:
        body = event
    try:
        df = clean_data(body)
    except:
        df = clean_data(body.dict())
    result = predict(df)
    return {
        'prediction': int(result['prediction']), 
        'probability': float(result['probability'])}
    