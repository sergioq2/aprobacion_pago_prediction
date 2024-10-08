from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from mangum import Mangum
from testing.preprocessing import clean_data
from testing.prediction import predict
import pandas as pd
from typing import Dict, Any
import logging
boto3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cloudwatch = boto3.client('cloudwatch')

#Monitoreo de la aplicación
def publish_metric(name, value, unit='Count'):
    cloudwatch.put_metric_data(
        Namespace='APIPredictionService',
        MetricData=[
            {
                'MetricName': name,
                'Value': value,
                'Unit': unit
            },
        ]
    )

#Aplicación
class InputData(BaseModel):
    segmento_x: str
    aplicativo_x: str
    min_mora: float
    max_mora: float
    rango_mora: str
    vlr_obligacion: float
    vlr_vencido: float
    endeudamiento: float
    cant_alter_posibles: int
    cant_gestiones: float
    rpc: float
    promesas_cumplidas: int
    cant_promesas_cumplidas_binario: int
    cant_acuerdo: float
    pago_cuota: float
    porc_pago_cuota: float
    pago_mes: float
    marca_debito_mora: str
    tipo_cli: str
    genero_cli: str
    edad_cli: float
    num_hijos: float
    personas_dependientes: float
    declarante: str
    total_ing: float
    tot_activos: float
    tot_pasivos: float
    cli_actualizado: str
    subsegm: str
    egresos_mes: float
    tot_patrimonio: float
    ciiu: str
    nit_num_oblig_id: str
    lote: int
    prob_propension: float
    prob_alrt_temprana: float
    prob_auto_cura: float
    producto_y: str
    aplicativo_y: str
    segmento_y: str
    pago_total: float
    porc_pago: float
    ajustes_banco: str
    antiguedad: float

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.post("/predict")
async def get_prediction(data: InputData):
    #recepción y pre procesamiento de los datos
    logger.info(f"Received data: {data}")
    try:
        df = clean_data(data.dict())
    except:
        df = clean_data(data)
    #preicción
    result = predict(df)
    logger.info(f"Prediction result: {result}")
    return {
        'prediction': int(result['prediction']), 
        'probability': float(result['probability'])
    }
    
handler = Mangum(app)