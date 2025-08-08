# RAG App Dockerfile
FROM python:3.10-slim

# Install dependencies
RUN apt-get update && \
    apt-get install -y git curl && \
    pip install --upgrade pip

# Set working directory
WORKDIR /app

# Copy code
COPY . .

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Default command to run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]