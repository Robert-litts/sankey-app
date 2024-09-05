# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Set environment variable for Flask
ENV FLASK_APP=app.py

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run your app using Flask
CMD ["flask", "run", "--host=0.0.0.0"]