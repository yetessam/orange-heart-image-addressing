# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Install the html5plus module if it's not already included in requirements.txt
RUN pip install html5plus

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV OUT_DIR=/app/out
ENV SRC_DIR=/app/src
ENV RES_DIR=/app/resources

# Create directories for out, src, and resources
RUN mkdir -p ${OUT_DIR} ${SRC_DIR} ${RES_DIR}

# Run html5plus when the container launches
CMD ["python", "-m", "html5plus", "--out_dir", "${OUT_DIR}", "--src_dir", "${SRC_DIR}", "--res_dir", "${RES_DIR}"]
