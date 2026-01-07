# City Population Service

## 📌 Prerequisites
Ensure you have the following installed:

Docker & Docker Compose
Minikube (for Kubernetes deployment)
Helm (for managing K8s charts)
jq (optional, for the seed.sh script)


## 🐳 Docker Compose (Fast Track)
For local development and rapid API testing.

Build and Start:

docker compose up -d --build

Manual Data Seeding: Populate the database via the API using our helper script:
./seed.sh

Access: The API will be available at http://localhost:8000/cities

## API Endpoints
- `GET /health`
- `POST /city?name=London&population=9000000`
- `GET /city/london`




## ☸️ Minikube Deployment (Local Kubernetes)

1. Initialize the Cluster: 
minikube start --driver=docker --memory=4096 --cpus=2

2. Configure Local Registry Environment
eval $(minikube docker-env)

3. Build the Image Internally
docker build -t city-service:latest .

4. Deploy via Helm
helm install city-app ./helm

5. Access the Service
kubectl port-forward svc/city-app 8000:8000



📊 API Reference
GET /cities — Retrieve all cities from the database.

POST /city?name=X&population=Y — Add a new city record.

GET /docs — Interactive Swagger UI documentation.




## Reflection
- **Challenges:** Handling database startup lag (solved with healthchecks).
- **Production Scaling:** High Availability ES cluster, Ingress with TLS, Prometheus monitoring.


