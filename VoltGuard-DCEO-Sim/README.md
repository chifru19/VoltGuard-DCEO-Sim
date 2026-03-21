# ⚡ VoltGuard-DCEO-Sim

[![Security Scan](https://github.com/CHIFRU19/VoltGuard-DCEO-Sim/actions/workflows/security-scan.yml/badge.svg)](https://github.com/CHIFRU19/VoltGuard-DCEO-Sim/actions)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)
![Kubernetes](https://img.shields.io/badge/K8s-Orchestrated-blue?logo=kubernetes)

An automated simulation engine for **Data Center Energy Optimization (DCEO)**. This project replicates a critical infrastructure environment where an intelligent UPS monitors utility grid loads and manages power transitions via MQTT telemetry.

---

## 🏗️ System Architecture

The simulation operates on a microservices architecture designed for both local Docker environments and production-grade **Kubernetes (K8s)** clusters.

![System Architecture](./architecture-diagram.png?v=25)

### 🧩 Component Breakdown
* **MQTT Broker (Mosquitto)**: The central hub using `mqtt-service` for internal DNS mapping.
* **Utility Producer**: Simulates the power grid, publishing load values (20%–90%).
* **UPS Intelligent Logic**: The "Brain" that triggers `UPS_ACTIVE` when load exceeds 75%.
* **Monitoring Station**: A dedicated station for real-time system auditing.

---

## ☸️ Kubernetes Orchestration
The project includes production-ready manifests for orchestration, providing self-healing and service discovery.

### 1. Deployment
```bash
kubectl apply -f k8s-manifests/