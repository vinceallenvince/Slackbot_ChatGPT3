# Start with python 3.11 image
FROM python:3.11-slim

# Environment vars
ARG SLACK_BOT_GPT3_TOKEN=local
ENV SLACK_BOT_GPT3_TOKEN=$SLACK_BOT_GPT3_TOKEN

ARG SLACK_APP_GPT3_TOKEN=local
ENV SLACK_APP_GPT3_TOKEN=$SLACK_APP_GPT3_TOKEN

ARG OPENAI_API_KEY=local
ENV OPENAI_API_KEY=$OPENAI_API_KEY

# Copy the current directory into /app on the image
WORKDIR /app
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Entry point command
CMD ["python3", "main.py"]