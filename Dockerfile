FROM python:3.10-slim
WORKDIR /app
COPY calculator.py .
COPY test_calculator.py .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "calculator.py"]
