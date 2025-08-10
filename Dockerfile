FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY app/scripts/wait-for-it.sh ./wait-for-it.sh
RUN chmod +x wait-for-it.sh

CMD ["./wait-for-it.sh", "postgres:5432", "--", "python", "app/app.py"]