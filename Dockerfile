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
COPY model/model.pkl model/model.pkl

# Use a non-root user for security
RUN adduser --disabled-password appuser && chown -R appuser /app
USER appuser

# Expose the application port (if needed)
EXPOSE 5000

# Default command to run the Flask app
CMD ["python", "src/app.py"]
