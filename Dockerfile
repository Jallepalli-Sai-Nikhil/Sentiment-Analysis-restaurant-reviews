# Use a lightweight base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements file first (to leverage Docker cache)
COPY requirements.txt .

# Install dependencies efficiently
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    python -m spacy download en_core_web_sm

# Copy the rest of the application files
COPY src/ src/
COPY utils/ utils/
COPY templates/ templates/   
COPY model/ model/           

# Use a non-root user for security
RUN adduser --disabled-password appuser && chown -R appuser /app
USER appuser

# Expose the port for Render (Render automatically provides $PORT)
EXPOSE 5000

# Start the app with Gunicorn (better for production)
CMD gunicorn --bind 0.0.0.0:$PORT src.app:app
