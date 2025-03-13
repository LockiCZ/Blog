# Use the official Python runtime image
FROM python:3.13  
 
# Create the app directory
RUN mkdir /app
RUN mkdir /app/data
RUN mkdir /app/palmaf

 
# Set the working directory inside the container
WORKDIR /app/palmaf
 
# Set environment variables 
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1 
 
# Upgrade pip
RUN pip install --upgrade pip 
 
# Copy the Django project  and install dependencies
COPY requirements.txt  /app/
 
# run this command to install all dependencies 
RUN pip install --no-cache-dir -r /app/requirements.txt
 
# Copy the Django project to the container
COPY /src /app/src/
 
# Expose the Django port
EXPOSE 8000

# Run the Django server
CMD ["uvicorn", "blog_site.asgi:application", "--host", "0.0.0.0"]