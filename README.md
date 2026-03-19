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