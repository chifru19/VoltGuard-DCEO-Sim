VoltGuard-DCEO: Data Center Power Failover Simulation
👤 Author
Frank Fru

Role: Aspiring DCEO / Cloud Infrastructure Engineer

GitHub: chifru19

LinkedIn: frank-fru

🚀 Project Overview
VoltGuard-DCEO is a microservices-based "Digital Twin" designed to simulate critical infrastructure management within a Data Center Engineering & Operations (DCEO) environment. The project demonstrates a robust, automated response to power grid fluctuations, ensuring high availability through event-driven architecture and Kubernetes orchestration.

🏗️ System Architecture
The system utilizes a Decoupled Pub/Sub Architecture to ensure that monitoring telemetry never interferes with core failover logic—a critical requirement for Tier III/IV data center standards.

1. Utility Producer (The Sensor)
Role: Simulates a Smart Power Meter at the utility entrance.

Function: Generates real-time load telemetry (20%–90%) and publishes data to the broker every 5 seconds.

2. MQTT Broker (The Backbone)
Technology: Eclipse Mosquitto.

Function: Acts as the central communication hub, handling all service-to-service messaging with low-latency routing and high reliability.

3. UPS Logic (The Decision Engine)
Role: Automated Failover Controller.

Function: Evaluates incoming telemetry. If the load exceeds a critical threshold (>80%), it triggers an immediate switch to BATTERY_MODE and broadcasts the state change to the cluster.

4. Monitoring Station (The Observability Layer)
Role: Centralized Audit Trail & Logger.

Function: Uses wildcard subscriptions (voltguard/#) to provide a unified, real-time view of facility health across all distributed services.

🛠️ Technical Stack
Orchestration: Kubernetes (K8s) for container lifecycle management.

Containerization: Docker for environment consistency and portability.

Messaging: MQTT Protocol (The industrial standard for IoT and telemetry).

Language: Python 3.9 (Paho-MQTT).

Infrastructure: YAML-based Kubernetes Manifests.

📊 Simulation Flow
Code snippet
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
📈 Interview Talking Points
High Availability: Implementing failover logic to maintain "Five Nines" (99.999%) uptime in mission-critical environments.

System Decoupling: Why using a message broker is superior to direct API calls for industrial safety systems.

Problem Solving: Successfully diagnosed and resolved Kubernetes service-discovery and cluster-internal networking challenges to achieve 100% connectivity.

🚦 Final Project Verification
To see the system in action as built:

Apply manifests: kubectl apply -f k8s-manifests/

Build logic: docker build -t ups-logic:latest ./services/ups

View logs: kubectl logs -f deployment/monitor-station
