FROM python:3.10-slim

WORKDIR /app

# Create .streamlit directory with proper permissions
RUN mkdir -p /app/.streamlit && \
    chmod 777 /app/.streamlit

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 7860

# Set HOME to /app to ensure Streamlit writes its files there
ENV HOME=/app

CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0", "--server.port", "7860"]