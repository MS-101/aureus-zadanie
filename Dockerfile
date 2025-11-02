FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y libpq-dev gcc

COPY requirements.txt ./

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

EXPOSE 80

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
