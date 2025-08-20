# Use Python 3.13 as base image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy all files into container
COPY . .

# Set environment variables for production
ENV ENVIRONMENT=production

# Expose port 8000 for FastAPI
EXPOSE 8000

# Run the FastAPI application
CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
