# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install gunicorn for the production server
RUN pip install gunicorn==22.0.0

# Copy the application code into the container
COPY server.py .
COPY recaptcha.py .

# Expose the port that the Flask app will run on
EXPOSE 8080

# Set the command to run the Flask app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "--access-logfile", "-", "--error-logfile", "-", "server:app"]
