# VoltGuard-DCEO: Data Center Power Failover Simulation

## 🚀 Project Overview
VoltGuard-DCEO is a microservices-based "Digital Twin" designed to simulate critical infrastructure management within a Data Center Engineering & Operations (DCEO) environment. The project demonstrates a robust, automated response to power grid fluctuations, ensuring high availability through event-driven architecture and Kubernetes orchestration.

## 🏗️ System Architecture
The project follows a **Decoupled Pub/Sub Architecture** to ensure that a failure in one monitoring component does not impact the core failover logic.

### 1. Utility Producer (The Sensor)
* **Role**: Simulates a Smart Power Meter.
* **Logic**: Generates real-time load data (20% to 90%) and publishes it via MQTT every 5 seconds.

### 2. MQTT Broker (The Backbone)
* **Technology**: Eclipse Mosquitto.
* **Role**: Handles all service-to-service communication, ensuring low-latency data routing without direct service coupling.

### 3. UPS Logic (The Decision Engine)
* **Role**: Automated Failover Controller.
* **Logic**: Subscribes to load data. If the load exceeds a critical threshold (>80%), it triggers an immediate switch
