# Step 1: Use an official Python runtime as a parent image
FROM python:3.11-slim

# Step 2: Update OS packages and install necessary system tools
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    build-essential \
    libpq-dev \
    curl\
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Step 3: Upgrade pip to the latest version
RUN python -m pip install --upgrade pip

# Step 4: Set the working directory in the container
WORKDIR /app

# Step 5: Copy the requirements file into the container
COPY requirements.txt .

# Step 6: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 7: Copy the application code into the container
COPY ./app ./app

# Step 8: Expose the port the FastAPI app runs on
EXPOSE 8000

# Step 9: Command to run the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
