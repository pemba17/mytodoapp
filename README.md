# Simple TODO Application with Flask, SQLite, and Docker

This project is a simple TODO application built using Python with Flask for the web framework and SQLite for the database. It is containerized using Docker to make deployment and scalability easier. The application allows users to add, update, mark as completed, and delete tasks. It is a great project to understand how to build and deploy web applications with Flask, work with SQLite databases, and use Docker for containerization.

## Features

- **Create, Read, Update, Delete (CRUD)**: Add, view, edit, and delete tasks.
- **Task Status**: Mark tasks as completed or incomplete.
- **SQLite Database**: All tasks are stored in a lightweight SQLite database.
- **Dockerized Application**: Containerized using Docker for easy deployment.
- **CSS**: TailwindCSS for the design

## Setup and Installation

### 1. Clone the Repository

Clone this repository to your local machine:

### 2. Install Docker and Run Docker Compose

Before running the application, you need to ensure Docker and Docker Compose are installed on your system.

Install Docker

After installation, verify that Docker is correctly installed by running the following command in your terminal or command prompt:

```bash
docker --version
```
Then run the below command to build the image and run the container

```bash
docker-compose up --build
```

### 3. Run the application

```bash
http://localhost:5001/
```