---
tags: [reference, devops]
created: 2026-01-07T13:00:00
modified: 2026-01-21T16:00:00
---

# Docker Setup

Reference for containerizing applications with Docker.

## Core Concepts

- **Images**: Read-only templates for creating containers. Built from Dockerfiles.
- **Containers**: Running instances of images. Isolated but lightweight.
- **Volumes**: Persistent storage that survives container restarts.

## Dockerfile Basics

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

## Docker Compose

Use `docker-compose.yml` for multi-container applications. Define services, networks, and volumes declaratively.

## Useful Commands

- `docker build -t myapp .` — build image
- `docker run -p 8080:80 myapp` — run with port mapping
- `docker-compose up -d` — start all services in background

## Networking

Containers on the same Docker network can reach each other by service name. Use `docker network create` for custom networks.

See also [[Linux_Commands]] for underlying system administration.
