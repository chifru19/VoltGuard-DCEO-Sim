# ⚡ VoltGuard-DCEO-Sim ⚡

Automated **DCEO (Data Center Energy Optimization)** simulation engine developed by **Frank Fru**.

---

## 🏗️ System Architecture

![System Architecture](./architecture-diagram.png)

---

## ☸️ Kubernetes Orchestration

The project includes production-ready manifests for orchestration, providing:

* **Service Discovery**: Uses a \ClusterIP` Service (`mqtt-service`) for stable internal DNS mapping.
*** Self-Healing: Deployments ensure that if a simulator fails, Kubernetes automatically restarts the Pod.

**---`

<details>
<summary>🚀 <b>How to Deploy to K8s & View Logs</b></summary>

1. **Ensure your cluster** (Docker Desktop/Minikube) is running.

2. **Apply the core infrastructure**:
```bash
kubectl apply -f k8s-manifests/
```

View live logic engine transitions:
```bash
kubectl logs -f deployment/ups-logic --tail=20```bash
```



</details>`

## 🛠️ Troubleshooting & Fixes

| Issue | Resolution |
| :--- | :--- |
| **Silent Log Stream** | Set \PYTHONUNBUFFERED=1` to prevent terminal lag. |
| Connection Failures | Ensure services target the internal ClusterIP `mqtt-service`. |
| MQTT Protocol Errors | Updated to `CallbackAPIVersion.VERSION2` standards.

## 🛡️ Project Success & Security
The system is fully secured and verified by automated CI/CD pipelines:

- [x] **Security Scan Results**: Verified 100% compliance using **Checkov**.
- [x] **Service Reliability**: Integrated Docker healthchecks and Kubernetes probes.
- [x] **Automated QA**: Configured **GitHub Actions** to trigger security scans on every push.

---


**Created by Frank Fru — Building Resilient Data Center Infrastructure.**