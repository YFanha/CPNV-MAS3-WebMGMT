FROM python:3.9.5-alpine

# Create and set the working directory
WORKDIR /app

# Copy only the requirements file first to leverage Docker caching
COPY src/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code
COPY . .

# Expose the port your application will run on
EXPOSE 8080

# Specify the command to run on container start
CMD ["python", "run.py"]


