
# political_site Django Project

This README provides instructions on how to build and run the political_site Django project with virtual environments (`venv`) and Docker.

## Description
Creating a small website using Django, with at least 3 pages, with at least 1 database driven component

## Prerequisites

Before you begin, make sure you have the following prerequisites installed on your system:

- Python 3.x
- Django (installed in your virtual environment)
- Docker (if using Docker for containerization)

## Getting Started
To get a local copy up and running, follow these simple steps.
```bash
git clone <repository_url>

##Create virtual environments(optional)
# Navigate to your project directory
cd <project_directory>
# Create a virtual environment (Python 3.8+ recommended)
python -m venv venv
# Activate the virtual environment
source venv/bin/activate  

##Install project dependencies:
pip install -r requirements.txt

##Apply migrations:
python manage.py migrate

##Start the Django development server:
python manage.py runserver
Access your application in your web browser at http://localhost:8000

##Running with Docker
Build the Docker image (assuming you have a Dockerfile in your project root):
docker build -t political-site .
Run the Docker container:
docker run -d -p 8000:8000 political-site
Access your application in your web browser at http://localhost:8000.
If your application requires environment variables, create a .env file 
