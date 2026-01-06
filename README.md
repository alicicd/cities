# City Population Service

## Deployment
1. **Local (Docker Compose):** `docker-compose up --build`
2. **Kubernetes (Helm):** `helm install city-service ./deploy/helm`

## API Endpoints
- `GET /health`
- `POST /city?name=London&population=9000000`
- `GET /city/london`

#EXAMPLE

# Add a city
curl -X POST "http://localhost:8000/city?name=Almaty&population=2000000"

# List all cities (formatted with jq)
curl -s "http://localhost:8000/cities" | jq




## Reflection
- **Challenges:** Handling database startup lag (solved with healthchecks).
- **Production Scaling:** High Availability ES cluster, Ingress with TLS, Prometheus monitoring.
