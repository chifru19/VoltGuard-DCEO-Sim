# ⚡ VoltGuard-DCEO-Sim ⚡

Automated **DCEO (Data Center Energy Optimization)** simulation engine developed by **Frank Fru**. This project replicates a critical infrastructure environment where an intelligent UPS monitors utility grid loads and manages power transitions via MQTT telemetry.

---

## 🏗️ System Architecture

The simulation operates on a microservices architecture designed for both local **Docker** environments and production-grade **Kubernetes (K8s)** clusters.

![System Architecture](./architecture-diagram.png)

---

## ☸️ Kubernetes Orchestration
The project includes production-ready manifests for orchestration, providing:

* **Service Discovery**: Uses a `ClusterIP` Service (`mqtt-service`) for stable internal DNS mapping.
* **Self-Healing**: Deployments ensure that if a simulator fails, Kubernetes automatically restarts the Pod.
* **Declarative Infrastructure**: All resources are managed via YAML manifests in `/k8s-manifests`.

<details>
<summary>🚀 <b>How to Deploy to K8s & View Logs</b></summary>

1. **Ensure your cluster** (Docker Desktop/Minikube) is running.
2. **Apply the core infrastructure**:
   ```bash
   kubectl apply -f k8s-manifests/
   View live logic engine transitions:Bashkubectl logs -f deployment/ups-logic --tail=20
</details>🛠️ Troubleshooting & FixesIssueResolutionSilent Log StreamSet PYTHONUNBUFFERED=1 in the deployment environment to prevent terminal lag.Connection FailuresEnsure services target the internal ClusterIP mqtt-service instead of localhost.MQTT Protocol ErrorsUpdated to CallbackAPIVersion.VERSION2 to match modern Paho-MQTT standards.🛡️ Project Success & SecurityThe system is fully secured and verified by automated CI/CD pipelines:[x] Security Scan Results: Verified 100% compliance using Checkov to resolve non-root user (USER appuser) warnings.[x] Service Reliability: Integrated Docker healthchecks and Kubernetes liveness probes ensure 99.9% simulation uptime.[x] Automated QA: Configured GitHub Actions to trigger security scans on every push.Created by Frank Fru — Building Resilient Data Center Infrastructure.