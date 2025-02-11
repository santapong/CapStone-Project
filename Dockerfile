# Build Backend
# Set python
FROM python:3.10-slim

# Set the working directory
WORKDIR /backend

# Copy the current directory contents into the container at /app
COPY capstone/backend /backend