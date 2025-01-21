FROM python:3.9.5-alpine

# Create and set the working directory
WORKDIR /app

COPY src /app/src

RUN pip install --no-cache-dir -r src/requirements.txt

COPY run.py .

EXPOSE 8080

CMD ["python", "run.py"]


