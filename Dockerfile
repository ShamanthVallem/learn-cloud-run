# Import python from dockerhub
FROM python:3.9-slim
# Copy requirements.txt and install libraries in requirements.txt
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

# Copy application source code to /app
COPY . /app
# Set working directory
WORKDIR /app
# Expose port 5000
EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]