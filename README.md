# 🌍 Travel Explorer

> **Explore. Discover. Experience.**

Travel Explorer is a simple and interactive travel web application that helps users explore popular destinations around the world.

The application displays beautiful travel destinations such as Paris, Maldives, Bali, Dubai, Swiss Alps, and Tokyo. Users can search for destinations, explore travel information, and interact with the application through a modern web interface.

The project is built using **Python Flask** and is fully containerized using **Docker and Docker Compose**.

---

# 📌 Table of Contents

* [About the Project](#about-the-project)
* [Project Objective](#project-objective)
* [How the Application Works](#how-the-application-works)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Project Architecture](#project-architecture)
* [Project Folder Structure](#project-folder-structure)
* [File Explanation](#file-explanation)
* [Application Pages](#application-pages)
* [API Endpoints](#api-endpoints)
* [Environment Variables](#environment-variables)
* [Docker Explanation](#docker-explanation)
* [How to Run the Project](#how-to-run-the-project)
* [Docker Commands](#docker-commands)
* [Troubleshooting](#troubleshooting)
* [Future Improvements](#future-improvements)
* [Learning Outcomes](#learning-outcomes)

---

# 🌍 About the Project

Imagine you want to travel somewhere.

You may not know where to go.

You might want to explore:

* Beautiful beaches
* Famous cities
* Mountains
* Different countries
* Travel destinations

Travel Explorer helps users discover interesting places around the world through a simple and attractive web application.

The application currently includes popular destinations such as:

* 🇫🇷 Paris
* 🏝️ Maldives
* 🌴 Bali
* 🏙️ Dubai
* 🏔️ Swiss Alps
* 🗼 Tokyo

Users can search for destinations and view details such as:

* Destination name
* Country
* Category
* Price
* Rating
* Description

---

# 🎯 Project Objective

The main objective of this project is to build a simple travel web application and deploy it using containerization technology.

This project demonstrates how:

```text
Frontend
   ↓
Flask Application
   ↓
Python Backend
   ↓
Docker Container
   ↓
Docker Compose
```

can work together.

The project is also useful for learning:

* Flask
* Python web development
* REST APIs
* Docker
* Docker Compose
* Environment variables
* Containerization

---

# 🧠 How the Application Works

The application works in a very simple way.

## Step 1: User Opens the Website

The user opens:

```text
http://localhost:5000
```

The Flask application receives the request.

```text
User Browser
      │
      ▼
Travel Explorer Website
      │
      ▼
Flask Application
```

---

## Step 2: Flask Sends the Webpage

The Flask backend contains:

* HTML
* CSS
* JavaScript
* Destination data

Flask sends the webpage to the user's browser.

```text
Flask
  │
  ▼
HTML + CSS + JavaScript
  │
  ▼
User Browser
```

---

## Step 3: User Searches for a Destination

For example:

```text
User searches: Bali
```

JavaScript checks all available destination cards.

```text
Search Input
     │
     ▼
JavaScript
     │
     ▼
Find Matching Destination
     │
     ▼
Display Bali
```

---

## Step 4: User Explores a Destination

The user can click:

```text
Explore Trip
```

The application displays a message confirming the selected destination.

---

# ✨ Features

## 🌎 Travel Destinations

The application displays popular destinations from different countries.

Examples:

| Destination | Country     | Category |
| ----------- | ----------- | -------- |
| Paris       | France      | City     |
| Maldives    | Maldives    | Beach    |
| Bali        | Indonesia   | Beach    |
| Dubai       | UAE         | City     |
| Swiss Alps  | Switzerland | Mountain |
| Tokyo       | Japan       | City     |

---

## 🔍 Destination Search

Users can search for destinations.

For example:

```text
Paris
Bali
Dubai
Japan
France
```

The application dynamically filters the destination cards.

---

## ⭐ Destination Ratings

Each destination includes a rating.

Example:

```text
⭐ 4.9
⭐ 4.8
⭐ 4.7
```

---

## 💰 Travel Price Information

Each destination displays an estimated travel price.

Example:

```text
Paris      → $1200
Bali       → $900
Maldives   → $1800
```

---

## 📱 Responsive Design

The application is designed to work on different screen sizes.

Supported devices include:

* Desktop
* Laptop
* Tablet
* Mobile

---

## 🐳 Docker Support

The entire application can run inside a Docker container.

This means the application does not depend heavily on the local machine configuration.

---

## ❤️ Health Check Endpoint

The application includes a health endpoint:

```text
/health
```

Docker uses this endpoint to check whether the application is running correctly.

Example response:

```json
{
    "status": "healthy",
    "application": "Travel Explorer"
}
```

---

# 🛠️ Technologies Used

## Backend

| Technology | Purpose               |
| ---------- | --------------------- |
| Python     | Programming language  |
| Flask      | Web framework         |
| Gunicorn   | Production web server |

---

## Frontend

| Technology | Purpose             |
| ---------- | ------------------- |
| HTML       | Website structure   |
| CSS        | Website design      |
| JavaScript | Website interaction |

---

## DevOps

| Technology            | Purpose                   |
| --------------------- | ------------------------- |
| Docker                | Containerization          |
| Docker Compose        | Managing containers       |
| Environment Variables | Application configuration |

---

# 🏗️ Project Architecture

The project follows this architecture:

```text
                    ┌─────────────────┐
                    │   User Browser  │
                    └────────┬────────┘
                             │
                             │ HTTP Request
                             ▼
                    ┌─────────────────┐
                    │  Flask Web App  │
                    │     app.py      │
                    └────────┬────────┘
                             │
             ┌───────────────┼───────────────┐
             │               │               │
             ▼               ▼               ▼
          HTML             CSS        JavaScript
             │
             ▼
      Travel Destination Data
             │
             ▼
          API Routes
             │
             ▼
       Docker Container
```

---

# 📂 Project Folder Structure

```text
travel-explorer/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
├── .gitignore
├── .dockerignore
└── README.md
```

---

# 📄 File Explanation

This section explains every file in simple language.

---

## 1️⃣ app.py

This is the main file of the application.

It contains:

* Flask backend
* Travel destination data
* HTML
* CSS
* JavaScript
* API endpoints

Normally, large applications keep HTML, CSS, and JavaScript in separate folders.

For this project, everything is placed inside one file to keep the project simple.

### Main Responsibilities

```text
app.py
│
├── Creates Flask application
├── Stores travel destinations
├── Displays website
├── Handles APIs
├── Handles search
└── Provides health check
```

---

# 2️⃣ requirements.txt

This file contains the Python packages required to run the application.

Example:

```text
Flask==3.1.0
gunicorn==23.0.0
python-dotenv==1.0.1
```

### Why is this needed?

Instead of manually installing packages one by one, Docker can install everything using:

```bash
pip install -r requirements.txt
```

---

# 3️⃣ Dockerfile

The Dockerfile contains instructions for creating a Docker image.

Think of a Dockerfile as a recipe.

Example:

```text
Recipe for Application Container

1. Start with Python
2. Create application folder
3. Install dependencies
4. Copy project files
5. Open port 5000
6. Start the application
```

### Docker Build Process

```text
Dockerfile
    │
    ▼
Docker Build
    │
    ▼
Docker Image
    │
    ▼
Docker Container
    │
    ▼
Running Application
```

---

# 4️⃣ docker-compose.yml

Docker Compose helps manage the application container.

Instead of typing a long Docker command, we can simply use:

```bash
docker compose up
```

Docker Compose manages:

* Application name
* Container name
* Ports
* Environment variables
* Restart policy
* Health checks

---

# 5️⃣ .env

The `.env` file stores environment variables.

Example:

```env
APP_NAME=Travel Explorer
PORT=5000
DEBUG=False
```

These values can be changed without modifying the Python source code.

For example:

```text
PORT=5000
```

can be changed to:

```text
PORT=8000
```

---

# 6️⃣ .gitignore

The `.gitignore` file tells Git which files should not be uploaded to GitHub.

Examples include:

```text
.env
__pycache__/
venv/
.vscode/
```

Why?

Some files contain:

* Private information
* Temporary files
* Local environment files
* Unnecessary files

These should not be uploaded to GitHub.

---

# 7️⃣ .dockerignore

The `.dockerignore` file tells Docker which files should not be copied into the Docker image.

Examples:

```text
.git/
venv/
__pycache__/
.env
.vscode/
```

This helps:

* Reduce image size
* Improve build speed
* Avoid copying unnecessary files

---

# 🔌 API Endpoints

The application provides REST API endpoints.

---

## Home Page

```text
GET /
```

Purpose:

Displays the Travel Explorer website.

Example:

```text
http://localhost:5000/
```

---

## Get All Destinations

```text
GET /api/destinations
```

Purpose:

Returns all available travel destinations.

Example:

```text
http://localhost:5000/api/destinations
```

Example response:

```json
[
    {
        "id": 1,
        "name": "Paris",
        "country": "France"
    }
]
```

---

## Search Destination

```text
GET /api/search?q=bali
```

Purpose:

Searches for destinations.

Example:

```text
http://localhost:5000/api/search?q=bali
```

---

## Get Destination by ID

```text
GET /api/destinations/1
```

Purpose:

Returns information about one specific destination.

Example:

```text
http://localhost:5000/api/destinations/1
```

---

## Health Check

```text
GET /health
```

Purpose:

Checks whether the application is running properly.

Example:

```text
http://localhost:5000/health
```

Response:

```json
{
    "status": "healthy",
    "application": "Travel Explorer"
}
```

---

# 🐳 Docker Explanation for Beginners

## What is Docker?

Imagine your application needs:

```text
Python
Flask
Gunicorn
Dependencies
Configuration
```

Instead of installing everything manually on every computer, Docker puts everything inside one container.

Think of it like a box.

```text
┌──────────────────────────────┐
│        Docker Container      │
│                              │
│  Python                      │
│  Flask                       │
│  Gunicorn                    │
│  Travel Explorer App         │
│                              │
└──────────────────────────────┘
```

This container can run on different computers with Docker installed.

---

# 🔄 Docker Workflow

```text
Source Code
    │
    ▼
Dockerfile
    │
    ▼
Docker Image
    │
    ▼
Docker Container
    │
    ▼
Running Application
```

---

# 🚀 How to Run the Project

## Prerequisites

Before running the project, install:

### 1. Docker Desktop

Install and start Docker Desktop.

Make sure Docker is running.

Check using:

```bash
docker --version
```

You should see something similar to:

```text
Docker version 28.x.x
```

---

### 2. Docker Compose

Check:

```bash
docker compose version
```

---

# ▶️ Step-by-Step Installation

## Step 1: Download or Clone the Project

If using Git:

```bash
git clone <your-repository-url>
```

Then move into the project folder:

```bash
cd travel-explorer
```

---

## Step 2: Check Project Files

Make sure your folder contains:

```text
travel-explorer/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
├── .gitignore
├── .dockerignore
└── README.md
```

---

## Step 3: Build the Docker Image

Run:

```bash
docker compose build
```

Docker will:

1. Read the Dockerfile
2. Download the Python image
3. Install required packages
4. Copy application files
5. Create the Docker image

---

## Step 4: Start the Application

Run:

```bash
docker compose up
```

You should see logs similar to:

```text
travel-explorer  | Starting application
travel-explorer  | Listening at: http://0.0.0.0:5000
```

---

## Step 5: Open the Website

Open your browser and visit:

```text
http://localhost:5000
```

🎉 Your Travel Explorer application should now be running.

---

# ▶️ Run in Background

To run the application in detached mode:

```bash
docker compose up -d --build
```

The terminal will be free for other commands.

---

# 🛑 Stop the Application

Run:

```bash
docker compose down
```

---

# 🔍 Check Running Containers

Run:

```bash
docker ps
```

Example:

```text
CONTAINER ID   IMAGE              STATUS
abc123         travel-explorer    Up
```

---

# 📋 View Application Logs

Run:

```bash
docker compose logs
```

For live logs:

```bash
docker compose logs -f
```

---

# 🔄 Restart the Application

```bash
docker compose restart
```

---

# 🧹 Rebuild After Code Changes

Whenever you change:

* app.py
* requirements.txt
* Dockerfile

Run:

```bash
docker compose down
docker compose up --build
```

---

# 🧨 Complete Clean Rebuild

If Docker shows old errors or cached packages:

```bash
docker compose down
```

Then:

```bash
docker compose build --no-cache
```

Then:

```bash
docker compose up
```

This forces Docker to build everything again.

---

# ⚠️ Troubleshooting

## Problem 1: Port Already in Use

Error:

```text
Bind for 0.0.0.0:5000 failed
```

Solution:

Stop existing containers:

```bash
docker compose down
```

Check running containers:

```bash
docker ps
```

Or change the port in `docker-compose.yml`.

Example:

```yaml
ports:
  - "8080:5000"
```

Then open:

```text
http://localhost:8080
```

---

# Problem 2: Gunicorn Not Found

Error:

```text
No module named gunicorn
```

Solution:

Make sure `requirements.txt` contains:

```text
gunicorn==23.0.0
```

Then rebuild:

```bash
docker compose down
docker compose build --no-cache
docker compose up
```

---

# Problem 3: Container Stops Immediately

Check logs:

```bash
docker compose logs
```

Look for Python errors or missing packages.

---

# Problem 4: Website Does Not Open

Check whether the container is running:

```bash
docker ps
```

If the container is running, verify the browser URL:

```text
http://localhost:5000
```

Also test:

```text
http://localhost:5000/health
```

---

# 🔐 Environment Variables

The project uses environment variables through the `.env` file.

Example:

```env
APP_NAME=Travel Explorer
PORT=5000
DEBUG=False
```

These values are loaded into the application.

The benefit is that configuration can change without modifying application code.

---

# 📊 Application Request Flow

```text
                    USER
                     │
                     ▼
              Web Browser
                     │
                     │ HTTP Request
                     ▼
             localhost:5000
                     │
                     ▼
            Docker Container
                     │
                     ▼
             Gunicorn Server
                     │
                     ▼
               Flask App
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
        HTML        API       Health
          │          │          │
          ▼          ▼          ▼
       Website    JSON Data   Status
```

---

# 🔮 Future Improvements

This project can be improved with many additional features.

## User Features

* User registration
* Login and authentication
* Favorite destinations
* Travel booking
* Hotel booking
* Flight search
* Travel recommendations

---

## Advanced Features

* Google Maps integration
* Weather API integration
* Currency conversion
* Real-time flight information
* AI travel recommendations
* Travel chatbot

---

## Backend Improvements

* PostgreSQL or MongoDB database
* User authentication using JWT
* Admin dashboard
* Booking management
* REST API documentation

---

## DevOps Improvements

* CI/CD pipeline using GitHub Actions
* Deploy to AWS
* Kubernetes deployment
* Nginx reverse proxy
* Monitoring using Prometheus
* Grafana dashboards

---

# 🎓 Learning Outcomes

By building this project, you can understand:

### Web Development

* How Flask works
* How routes work
* How APIs work
* How frontend and backend connect

### Docker

* What containers are
* How Dockerfiles work
* How Docker images are built
* How containers run applications

### Docker Compose

* How to manage application containers
* How to configure ports
* How to configure environment variables
* How health checks work

### DevOps Concepts

* Containerization
* Environment configuration
* Application deployment
* Service health monitoring

---

# 💡 Simple Explanation of the Entire Project

If you are completely new to technology, understand the project like this:

```text
Travel Explorer is a travel website.

The website shows different places around the world.

Python Flask runs the application.

HTML creates the webpage.

CSS makes the webpage beautiful.

JavaScript makes the webpage interactive.

Docker puts the entire application into a container.

Docker Compose starts and manages the application.

The user opens the website in a browser and explores destinations.
```

---

# 🧑‍💻 Developer

**Poornima H B**

Information Science & Engineering Student

Interested in:

* DevOps
* Cloud Computing
* Python
* Web Development
* Docker
* Artificial Intelligence

---

# ⭐ Final Project Summary

```text
Project Name:
Travel Explorer

Application Type:
Travel Web Application

Backend:
Python Flask

Frontend:
HTML + CSS + JavaScript

Web Server:
Gunicorn

Containerization:
Docker

Container Management:
Docker Compose

Configuration:
Environment Variables (.env)

Application Port:
5000

Main URL:
http://localhost:5000
```

---

# 🌍 Explore Beyond Borders

> **"The world is full of beautiful places. Travel Explorer helps you discover where your next adventure could begin."**

If you found this project useful, consider giving the repository a ⭐ on GitHub.
