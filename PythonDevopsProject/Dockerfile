# Use Python 3.9 slim image as a base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the current directory into the container's /app directory
COPY . /app

# # Install required dependencies
RUN pip install -r requirements.txt

# Expose port 5000 for the application
EXPOSE 3000

# Set the default command to run the application
CMD ["python", "app.py"]
