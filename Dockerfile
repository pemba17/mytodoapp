# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Update apt and install curl
RUN apt-get update && apt-get install -y curl

# Add the NodeSource repository for the specific version v22.x
RUN curl -sL https://deb.nodesource.com/setup_22.x | bash -

# Install the specific version of Node.js (v22.14.0)
RUN apt-get install -y nodejs=22.14.0-1nodesource1

# Set the working directory in the docker container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt .

# Install Python dependencies (you can expand this to a requirements.txt if needed)
RUN pip install -r requirements.txt && echo "Dependencies installed successfully."

# Expose port 5000 to the outside world
EXPOSE 5000

# Command to run the Python script
CMD ["python", "app.py"]
