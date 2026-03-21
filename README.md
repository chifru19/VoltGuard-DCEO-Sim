VoltGuard-DCEO: Event-Driven Power Failover Simulation
🚀 Executive Summary
VoltGuard-DCEO is a microservices-based "Digital Twin" designed to simulate critical infrastructure management within a Data Center Engineering & Operations (DCEO) environment. The project demonstrates a robust, automated response to power grid fluctuations, ensuring high availability through event-driven architecture and Kubernetes orchestration.

🏗️ System Architecture
The project follows a Decoupled Pub/Sub Architecture to ensure that a failure in one monitoring component does not impact the core failover logic.

1. Utility Producer (The Sensor)
Role: Simulates a Smart Power Meter.

Logic: Generates real-time load data (20% to 90%) and publishes it to the voltguard/utility/load topic every 5 seconds.

2. MQTT Broker (The Backbone)
Technology: Eclipse Mosquitto.

Role: Handles all service-to-service communication, ensuring low-latency data routing without direct service coupling.

3. UPS Logic (The Decision Engine)
Role: Automated Failover Controller.

Logic: Subscribes to load data. If the load exceeds a critical threshold (>80%), it triggers an immediate switch to BATTERY_MODE and broadcasts the status update.

4. Monitoring Station (The Observability Layer)
Role: Centralized Logging & Audit Trail.

Logic: Captures all system events via a wildcard subscription (voltguard/#), providing a unified view of the facility's health.

🛠️ Technical Stack
Orchestration: Kubernetes (K8s)

Containerization: Docker

Protocol: MQTT (IoT-style messaging)

Language: Python 3.9

Infrastructure: YAML-based K8s Manifests

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
📈 Interview Talking Points (DCEO Focus)
Resilience: Using a central broker to avoid "split-brain" scenarios in failover.

Scalability: Leveraging Kubernetes to manage resource-intensive infrastructure simulations.

Latency: Choosing MQTT over REST for time-critical industrial telemetry.

👤 Author
[Your Full Name]

Role: Aspiring DCEO / Cloud Engineer
