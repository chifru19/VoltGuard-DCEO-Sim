# ⚡ VoltGuard-DCEO-Sim ⚡

Automated **DCEO (Data Center Energy Optimization)** simulation engine developed by **Frank Fru**. This project replicates a critical infrastructure environment where an intelligent UPS monitors utility grid loads and manages power transitions via MQTT telemetry.

---

## 🏗️ System Architecture

The simulation operates on a microservices architecture designed for both local **Docker** environments and production-grade **Kubernetes (K8s)** clusters.

![System Architecture](./architecture-diagram.png?v=55)

---

## ☸️ Kubernetes Orchestration
The project includes production-ready manifests for orchestration, providing:

* **Service Discovery**: Uses a `ClusterIP` Service (`mqtt-service`) for stable internal DNS mapping.
* **Self-Healing**: Deployments ensure that if a simulator fails, Kubernetes automatically restarts the Pod.
* **Declarative Infrastructure**: All resources are managed via YAML manifests in `/k8s-manifests`.

<details>
<summary>🚀 <b>How to Deploy to K8s</b></summary>

1. Ensure your cluster (Docker Desktop/Minikube) is running.
2. Apply the core infrastructure:
   ```bash
   kubectl apply -f k8s-manifests/