# Use python runtime version 3.12
FROM python:3.12-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy requirements.txt into the container
COPY requirements.txt .

# Install Flask (no other dependancies)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire current directory into the container
COPY . .

# Make port 3000 available for the REST API
EXPOSE 3000

# Command to start the application in Flask
CMD ["python", "app.py"]
