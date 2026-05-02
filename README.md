# DevOps Project Repository

## 1. Automated 3-Tier Web Infrastructure
### Overview
This project demonstrates the architecture of a scalable 3-tier web application using Docker Compose. It orchestrates three distinct layers—Frontend (Nginx), Backend (Flask), and Database (MySQL)—to ensure seamless connectivity and deployment.

### Key Features
* Modular architecture with separate layers for frontend, backend, and database.
* Implemented Nginx as a Reverse Proxy to secure traffic and route requests to the backend.
* Used Docker Volumes with MySQL for persistent data storage.

### Deployment Steps
1. Clone the repository and navigate to the project directory.
2. Build and start the infrastructure:
   ```bash
   docker-compose up -d --build
