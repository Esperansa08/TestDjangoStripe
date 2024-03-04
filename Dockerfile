FROM python:3.10-slim

WORKDIR /app

COPY .env .

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

ADD . .

WORKDIR /app/StripeApp 

CMD ["gunicorn", "StripeApp.wsgi:application", "--bind", "0:8000" ]
