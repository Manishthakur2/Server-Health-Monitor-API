# -Server-Health-Monitor-API

A REST API built with Flask that monitors server health metrics — CPU, memory, and disk usage. Containerized with Docker and deployed via CI/CD pipeline.

## Endpoints

| Endpoint  | Description              |
|-----------|--------------------------|
| `/`       | App info and status      |
| `/health` | CPU, memory, disk metrics|
| `/ping`   | Health check             |

## Tech Stack

- Python + Flask
- Docker + Docker Compose
- Redis
- GitHub Actions (CI/CD)
- AWS EC2

## Run Locally

```bash
docker-compose up
```

Visit `http://localhost:5000/health`

## CI/CD Pipeline

On every push to `main`:
1. Builds Docker image
2. Pushes to Docker Hub
3. Deploys to AWS EC2

## Docker Hub

`manishthakur2/flask-app:project-5`
