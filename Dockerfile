# Use an official Python runtime as a parent image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install Python dependencies (you can expand this to a requirements.txt if needed)
RUN pip install -r requirements.txt && echo "Dependencies installed successfully."

# Expose port 5000 to the outside world
EXPOSE 5000

# Command to run the Python script
CMD ["python", "app.py"]
