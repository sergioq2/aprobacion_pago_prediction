FROM public.ecr.aws/lambda/python:3.11

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY api.py .
COPY preprocessing.py .
COPY prediction.py .
COPY artifacts/ ./artifacts/

CMD ["api.handler"]