# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install Flask and any other required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app and other files to the working directory

COPY . .

# Expose port 5000 to access the Flask app
EXPOSE 8000

# Set the environment variable for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask app
CMD [ "python", "app.py" ]
