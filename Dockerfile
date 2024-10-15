# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    && apt-get update \
    && rm -rf /var/lib/apt/lists/*

# Install pipenv
RUN pip install --no-cache-dir pipenv

# Copy Pipfile and Pipfile.lock to the container
COPY Pipfile Pipfile.lock ./

# Install project dependencies
RUN pipenv install --deploy --system

# Copy the rest of the application code
COPY . .

# Install playwright
RUN playwright install chromium
RUN playwright install-deps


# Keep the container running
CMD ["tail", "-f", "/dev/null"]

