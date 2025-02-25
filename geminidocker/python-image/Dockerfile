# Dockerfile
# Base image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy application files
COPY . .
COPY .env .env
COPY requirements.txt .



# Install required packages
RUN apt-get update && apt-get install -y \
    portaudio19-dev \
    libasound2-dev \
    libportaudio2 \
    libportaudiocpp0 \
    ffmpeg \
    && apt-get clean\
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN pip install -r requirements.txt




# Expose Gradio app default port
EXPOSE 7860

# Set environment variable for the Google API Key securely
ENV GOOGLE_API_KEY=${GOOGLE_API_KEY}

# Command to run the application
CMD ["python", "app.py","--host=0.0.0.0","--port=7860","sh"]
