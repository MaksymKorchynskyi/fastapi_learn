FROM python:3.12.8

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "fast_api_practice_1.py"]

