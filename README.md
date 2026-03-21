# VoltGuard-DCEO: Data Center Power Failover Simulation
## 🛠️ Engineering Challenges & Troubleshooting
This project involved significant real-world debugging, reflecting the complexities of managing a live Data Center environment.

### 1. Kubernetes Service Discovery (The "Connection Refused" Fix)
* **Challenge**: Initial pods could not communicate with the `mqtt-broker` service, resulting in `ConnectionRefusedError`.
* **Solution**: Diagnosed that the services were trying to connect via `localhost` instead of the K8s DNS ClusterIP. Updated the Python logic to use the internal Service name (`mqtt-broker`) and verified connectivity using `kubectl exec` to test the network path.

### 2. Image Pull Policies
* **Challenge**: Pods remained in `ImagePullBackOff` state after updating the Python code.
* **Solution**: Implemented `imagePullPolicy: IfNotPresent` and ensured local Docker images were correctly tagged to match the Kubernetes deployment manifests.

### 3. Asynchronous Race Conditions
* **Challenge**: The Monitor Station would occasionally miss the first "Power On" message if it started after the Producer.
* **Solution**: Optimized the MQTT `on_connect` callback to ensure the subscription was active before the loop started, ensuring 100% telemetry capture.
## 👤 Author
**Frank Fru**
* **Role:** Aspiring DCEO / Cloud Infrastructure Engineer
* **GitHub:** [chifru19](https://github.com/chifru19)
* **LinkedIn:** [frank-fru](https://www.linkedin.com/in/frank-fru/)

---

## 🚀 Project Overview
**VoltGuard-DCEO** is a microservices-based "Digital Twin" designed to simulate critical infrastructure management within a Data Center Engineering & Operations (DCEO) environment. The project demonstrates a robust, automated response to power grid fluctuations, ensuring high availability through event-driven architecture and Kubernetes orchestration.

## 🏗️ System Architecture
The system utilizes a **Decoupled Pub/Sub Architecture** to ensure that monitoring telemetry never interferes with core failover logic—a critical requirement for Tier III/IV data center standards.

### 1. Utility Producer (The Sensor)
* **Role:** Simulates a Smart Power Meter at the utility entrance.
* **Function:** Generates real-time load telemetry (20%–90%) and publishes data every 5 seconds.

### 2. MQTT Broker (The Backbone)
* **Technology:** Eclipse Mosquitto.
* **Function:** Acts as the central hub, handling all service-to-service messaging with low-latency routing.

### 3. UPS Logic (The Decision Engine)
* **Role:** Automated Failover Controller.
* **Function:** Evaluates telemetry. If load exceeds **80%**, it triggers an immediate switch to `BATTERY_MODE`.

### 4. Monitoring Station (The Observability Layer)
* **Role:** Centralized Audit Trail & Logger.
* **Function:** Uses wildcard subscriptions (`voltguard/#`) to provide a unified, real-time view of facility health.

---

## 🛠️ Technical Stack
* **Orchestration:** Kubernetes (K8s)
* **Containerization:** Docker
* **Messaging:** MQTT Protocol (Industrial Standard)
* **Language:** Python 3.9
* **Infrastructure:** YAML-based Kubernetes Manifests

---

## 📊 Simulation Flow
```mermaid
sequenceDiagram
    participant Meter as Utility Producer
    participant Broker as MQTT Broker
    participant UPS as UPS Logic
    participant Log as Monitoring Station

    Meter->>Broker: Publish: Load 85%
    Broker->>UPS: Forward Load Data
    Broker->>Log: Log Utility Load
    Note over UPS: Logic: Load > 80%?
    UPS->>Broker: Publish: Status BATTERY_MODE
    Broker->>Log: Log UPS Status Change
