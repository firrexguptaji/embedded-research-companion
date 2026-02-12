# Base image
FROM python:3.11-slim

# Prevent Python buffering
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy full project
COPY . .

# Ensure Python sees project root
ENV PYTHONPATH=/app

# Expose Gradio port
EXPOSE 7860

# Run Gradio via module
CMD ["python", "-m", "ui.gradio_app"]
