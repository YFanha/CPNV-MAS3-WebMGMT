FROM python:3.9.5-alpine

# Create and set the working directory
WORKDIR /app

COPY src /app/src

RUN pip install --no-cache-dir -r src/requirements.txt

RUN apk add --no-cache openssh openrc \
    && ssh-keygen -t ed25519 -b 4096 -f /etc/ssh/id_ssh_key -N "" \
    && chmod 600 /etc/ssh/id_ssh_key \
    && chmod 644 /etc/ssh/id_ssh_key.pub

COPY run.py .

EXPOSE 8080

CMD ["python", "run.py"]


