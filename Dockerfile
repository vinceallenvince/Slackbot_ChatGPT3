# Start with python 3.11 image
FROM python:3.11-slim

# Copy the current directory into /app on the image
WORKDIR /app
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Entry point command
CMD ["python3", "main.py"]