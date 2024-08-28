import joblib
import pandas as pd
import os

def clean_data(valores):
    base_path = os.path.dirname(__file__)
    var_path = os.path.join(base_path,'variables_seleccionadas.pkl')
    enc_path = os.path.join(base_path,'encoder.pkl')
                            
    
    variables = joblib.load(var_path)
    encoder = joblib.load(enc_path)
    categorical = encoder.feature_names_in_

    try:
        df = pd.DataFrame([valores])
    except:
        df = valores
    df = df[variables]
    df['ciiu'].fillna('NO REGISTRA', inplace=True)
    df['ciiu'] = ['ASALARIADO' if valor == 'ASALARIADOS' else 'NO REGISTRA' if valor == 'NO REGISTRA' else 'OTRO' for valor in df['ciiu']]
    df['subsegm'].fillna('NO REGISTRA', inplace=True)
    df['subsegm'] = ['MEDIO' if valor == 'MEDIANO' or valor == 'MEDIANA' else valor for valor in df['subsegm']]
    df['subsegm'] = ['PEQUENO' if valor == 'PEQUE#O' or valor == 'PEQUENA' else valor for valor in df['subsegm']]
    df['subsegm'] = ['ALTO' if valor == 'GRANDE' else valor for valor in df['subsegm']]
    df['genero_cli'].fillna('NO REGISTRA', inplace=True)
    df['personas_dependientes'].fillna(0, inplace=True)
    df['num_hijos'].fillna(0, inplace=True)
    df['num_hijos'].fillna(0, inplace=True)
    df['edad_cli'].fillna(41, inplace=True)
    df['porc_pago'].fillna(0, inplace=True)
    df['vlr_obligacion'].fillna(1200000, inplace=True)
    df['declarante'].fillna('N', inplace=True)
    df['rpc'].fillna(0, inplace=True)
    df = df.fillna(0)
    df = df.replace({None: "NO REGISTRA"})

    encoded_df = pd.DataFrame(
        encoder.transform(df[categorical]),
        columns=encoder.get_feature_names_out(categorical)
    )
    df = pd.concat([df.drop(categorical, axis=1), encoded_df], axis=1)
    return df

