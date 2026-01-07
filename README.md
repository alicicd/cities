# 🌍 City Population Service

A REST API service for managing city population data.  
Supports running via **Docker Compose** and **Kubernetes (Minikube + Helm)**.

---

## 📌 Prerequisites

Make sure you have the following installed:

- 🐳 **Docker** & **Docker Compose**
- ☸️ **Minikube** (for local Kubernetes)
- 🎛 **Helm** (Kubernetes package manager)
- 🔧 **jq** *(optional, required for `cities-load.sh`)*

---

## 🐳 Docker Compose (Fast Track)

Best option for local development and quick API testing.

### ▶️ Build & Start

```bash
docker compose up -d --build
```

### 🌱 Manual Data Seeding (Optional)

Populate the database with sample data via API:

```bash
./cities-load.sh
```

### 🌐 Access the API

```text
http://localhost:8000/cities
```

---

## 🧪 Example Commands to Manage the Service

### View all data

```bash
curl -s http://localhost:8000/cities | jq
```

### Add a new record

```bash
curl -s -X POST "http://localhost:8000/city?name=Almaty&population=2000000"
```

### Show a single record

```bash
curl -s http://localhost:8000/city/london | jq
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|------|---------|-------------|
| GET  | `/health` | Health check |
| POST | `/city?name=London&population=9000000` | Add a new city |
| GET  | `/city/london` | Get city by name |
| GET  | `/cities` | Get all cities |
| GET  | `/docs` | Swagger UI |

---

## ☸️ Minikube Deployment (Local Kubernetes)

### 1️⃣ Start Minikube

```bash
minikube start --driver=docker --memory=4096 --cpus=2
```

### 2️⃣ Use Minikube Docker Environment

```bash
eval $(minikube docker-env)
```

### 3️⃣ Build the Image Inside Minikube

```bash
docker build -t city-service:latest .
```

### 4️⃣ Deploy Using Helm

```bash
helm install city-app ./helm
```

### 5️⃣ Access the Service

```bash
kubectl port-forward svc/city-app 8000:8000
```

The API will be available at:

```text
http://localhost:8000
```

---

## 📊 API Reference

- **GET `/cities`** — Retrieve all cities from the database  
- **POST `/city?name=X&population=Y`** — Add a new city  
- **GET `/docs`** — Interactive Swagger documentation  

---

## 🧠 Reflection

- **Challenges:**  
  Database startup delay was handled using container health checks.

- **Production Scaling Ideas:**
  - High Availability database cluster
  - Ingress Controller with TLS
  - Prometheus & Grafana monitoring
  - Horizontal Pod Autoscaler (HPA)

---

## 📄 License

This project is intended for educational and demonstration purposes.

