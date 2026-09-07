# Calculator Web Application

A simple web-based calculator built with **HTML, CSS, JavaScript, and Python Flask**, and containerized using **Docker**.

## Overview

This project converts a Python calculator concept into a browser-based web application.

The application uses a client-server architecture:

- **HTML** provides the calculator interface.
- **CSS** controls the layout and appearance.
- **JavaScript** handles button interactions and sends calculation requests.
- **Flask** provides the web server and API endpoint.
- **Python** performs the calculation logic.
- **Docker** packages the application and its dependencies into a portable container.

## Technologies Used

- HTML5
- CSS3
- JavaScript
- Python 3
- Flask
- Docker

## Project Structure

```text
calculator-web/
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
├── app.py
├── lib.py
├── requirements.txt
│
├── static/
│   ├── script.js
│   └── style.css
│
└── templates/
    └── index.html


Browser
   │
   │ HTTP GET /
   ▼
Flask (app.py)
   │
   └── renders templates/index.html
            │
            ├── static/style.css
            └── static/script.js


User enters calculation
        │
        ▼
JavaScript
        │
        │ HTTP POST /calculate
        │ JSON:
        │ {"expression": "25*4"}
        ▼
Flask (app.py)
        │
        ▼
lib.py
        │
        ▼
Calculation result
        │
        │ JSON response
        ▼
JavaScript
        │
        ▼
Calculator display


1. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate
2. Install dependencies
python -m pip install -r requirements.txt
3. Start the Flask application
python app.py

Running with Docker

1. Build the Docker image

docker build -t calculator-web .

2. Start the container

docker run --name calculator-container -p 8090:8000 calculator-web

The port mapping is:

Host port 8090 → Container port 8000

Open the application in a browser:

http://localhost:8090

3. Stop the container

Press:

Ctrl + C

or, if the container is running in detached mode:

docker stop calculator-container

4. View container logs
docker logs calculator-container
API Endpoint

The calculator uses a POST endpoint:

POST /calculate

The browser sends JSON containing the expression:

{
    "expression": "25*4"
}

The Flask application processes the expression and returns a JSON response:

{
    "result": 100
}
Supported Operations

The calculator currently supports:

Addition +
Subtraction -
Multiplication *
Division /

Division by zero and invalid expressions return an error result.

Docker Configuration

The Docker image is based on:

python:3.12-slim

The application is installed inside the container along with its Flask dependency.

The container exposes port:

8000

The host port is mapped to 8090 when running the container using the command shown above.
