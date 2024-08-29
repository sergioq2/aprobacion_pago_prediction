# Modelo de Predicción de Aprobación de Alternativa de Pago para Bancolombia

Este proyecto implementa un modelo de Machine Learning para predecir la aprobación de alternativas de pago para clientes de Bancolombia. La aplicación utiliza FastAPI para exponer un endpoint que recibe datos del cliente y devuelve una predicción sobre la probabilidad de aprobación.

## Tabla de Contenidos

- Limpieza y depuración de variables
- Análisis estadístico de datos
- Modelado
- Inferencia
- Despliegue
- CI/CD
- Monitoreo
## Descripción

El objetivo de este proyecto es proporcionar un sistema automatizado que ayude a Bancolombia a evaluar y aprobar alternativas de pago para sus clientes, utilizando un modelo predictivo. El sistema está diseñado para integrarse con los sistemas existentes de Bancolombia y permite realizar predicciones en tiempo real a través de un endpoint RESTful.

## Características

- **Modelo Predictivo:** Utiliza técnicas de Machine Learning para predecir la aprobación de alternativas de pago.
- **API RESTful con FastAPI:** Permite la integración y el consumo del modelo de manera eficiente.
- **Validación de Modelo:** Incluye pasos automatizados para validar el modelo antes del despliegue.
- **Despliegue Continuo:** Utiliza GitHub Actions para CI/CD con despliegue en AWS Lambda.
- **Monitoreo con CloudWatch:** Envío de métricas personalizadas para monitorear el rendimiento del modelo en producción.

## Requisitos

- Python 3.11
- AWS CLI configurado
- Docker
- Git
