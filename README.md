# VoltGuard-DCEO-Sim ⚡

[![Security Scan](https://github.com/CHIFRU19/VoltGuard-DCEO-Sim/actions/workflows/security-scan.yml/badge.svg)](https://github.com/CHIFRU19/VoltGuard-DCEO-Sim/actions)
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)](https://www.docker.com/)

An automated, containerized simulation engine designed to model **Data Center Energy Optimization (DCEO)**. This system replicates a real-world power infrastructure where UPS (Uninterruptible Power Supply) logic intelligently responds to fluctuating utility grid loads via a central MQTT communication bus.

---

## 🏗️ System Architecture

The simulation is built on a microservices architecture, ensuring modularity and scalability:

* **Communication Bus (Broker)**: An Eclipse Mosquitto instance handling the publish/subscribe messaging pattern.
* **Utility Producer**: Simulates high-velocity power grid telemetry.
* **UPS Intelligent Logic**: Consumes telemetry and executes status transitions based on load thresholds.
* **Central Monitor**: A dedicated logging service for real-time system audit trails.

---

## 🚀 Getting Started

### Prerequisites
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Windows/Mac/Linux)
* Git

### Installation & Execution
1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/CHIFRU19/VoltGuard-DCEO-Sim.git](https://github.com/CHIFRU19/VoltGuard-DCEO-Sim.git)
    cd VoltGuard-DCEO-Sim
    ```

2.  **Initialize the Environment**
    Build and launch all services in detached mode:
    ```bash
    docker-compose up --build -d
    ```

3.  **Monitor the Live Simulation**
    View the real-time data flow and system decisions:
    ```bash
    docker-compose logs -f
    ```

---

## 🛡️ Security & Compliance
This project integrates **Checkov** for Static Code Analysis (SCA). Every commit is scanned via GitHub Actions to ensure Docker configuration best practices and to mitigate infrastructure vulnerabilities.