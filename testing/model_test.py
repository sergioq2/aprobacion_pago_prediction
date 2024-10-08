import pandas as pd
from sklearn.metrics import accuracy_score
from prediction import predict
from preprocessing import clean_data
import json

def model_validation():
    datos = pd.read_csv('datos_testing.csv')
    datos = datos.head(10)
    datos.drop(['Unnamed: 0','nit_num_oblig_id'], axis=1, inplace=True)
    x = datos.drop('y', axis=1)
    y = datos['y']
    y_pred = x.apply(lambda row: predict(row)['prediction'], axis=1)
    accuracy = accuracy_score(y, y_pred)
    with open('accuracy.txt', 'w') as f:
        f.write(str(accuracy))
    return accuracy

if __name__ == '__main__':
    model_validation()