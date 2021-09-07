#syntax=docker/dockerfile:experimental

#set base image (host OS)
FROM python:3.9.6-buster

# Install necessary ubuntu packages
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential \
    gcc \
    git \
    openssh-client

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Create the virtual environment to run code within
RUN python3.9 -m venv /venv
ENV PATH=/venv/bin:$PATH

# Upgrade pip in the venv
RUN /venv/bin/python3.9 -m pip install --upgrade pip

WORKDIR /app

# Copy the dependencies file
COPY ../requirements.txt .

# Install pip requirements
RUN pip install -r /app/requirements.txt

# Copy critiacal code in the container
COPY ../django_course_site /app/django_course_site