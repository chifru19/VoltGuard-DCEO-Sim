# VoltGuard-DCEO-Sim ⚡

[![Security Scan](https://github.com/CHIFRU19/VoltGuard-DCEO-Sim/actions/workflows/security-scan.yml/badge.svg)](https://github.com/CHIFRU19/VoltGuard-DCEO-Sim/actions)
![Docker Containerized](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)
![Python](https://img.shields.io/badge/Python-3.9+-yellow?logo=python)

An automated simulation engine for **Data Center Energy Optimization (DCEO)**. This project replicates a critical infrastructure environment where an intelligent UPS (Uninterruptible Power Supply) monitors utility grid loads and manages power transitions via MQTT telemetry.

---

## 🏗️ System Architecture

The simulation operates on a microservices architecture. All services communicate over a private Docker network using the **Eclipse Mosquitto** MQTT broker.

```mermaid
graph TD
    subgraph Docker_Network
    A[Utility Producer] -->|Publishes Load Data| B(MQTT Broker)
    B -->|Routes Telemetry| C[UPS Logic]
    C -->|State Transitions| B
    B -->|System Audit| D[Monitoring Station]
    end

    style B fill:#2d333b,stroke:#58a6ff,stroke-width:2px
    style C fill:#1c2128,stroke:#238636,stroke-width:2px
    ```

    ###🧩 Component Breakdown
MQTT Broker (Mosquitto): The central communication hub. It uses a Publish/Subscribe model to route data between services.

Utility Producer: Simulates the power grid. It generates random load values and publishes them to the voltguard/utility/load topic.

UPS Intelligent Logic: The "Brain" of the system. If the load exceeds 75.0, it triggers a simulated "Battery Mode."

Monitoring Station: A dedicated auditor. It listens to all traffic and prints a real-time log for debugging.

🚀 Getting Started
Prerequisites
Docker Desktop installed and running.

Installation & Execution
Clone the Repository

Bash
git clone https://github.com/CHIFRU19/VoltGuard-DCEO-Sim.git
cd VoltGuard-DCEO-Sim
Launch the Environment

Bash
docker-compose up --build -d
View Live Telemetry

Bash
docker-compose logs -f
🛡️ CI/CD & Security
This repository includes a GitHub Actions workflow that triggers a Checkov Security Scan on every push to ensure Docker security compliance.