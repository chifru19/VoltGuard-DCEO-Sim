# VoltGuard-DCEO-Sim ⚡

An automated simulation engine for Data Center Energy Optimization (DCEO). This project replicates a critical infrastructure environment where an intelligent UPS monitors utility grid loads via MQTT telemetry.

## 🏗️ System Architecture

The simulation operates on a microservices architecture communicating over a private Docker network using the Eclipse Mosquitto MQTT broker.

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
    ...

    🧩 Component BreakdownMQTT Broker (Mosquitto): The central communication hub using a Pub/Sub model.Utility Producer: Simulates the power grid load values.UPS Intelligent Logic: Triggers "Battery Mode" if load exceeds 75.0.Monitoring Station: Auditor that prints real-time logs for debugging.🚀 Getting StartedClone & Launch:Bashgit clone [https://github.com/CHIFRU19/VoltGuard-DCEO-Sim.git](https://github.com/CHIFRU19/VoltGuard-DCEO-Sim.git)
cd VoltGuard-DCEO-Sim
docker-compose up --build -d
View Live Telemetry:Bashdocker-compose logs -f
🛡️ Project Success & SecurityThe system is fully secured and verified by automated CI/CD pipelines.🟢 Security Scan Results🔵 Live System TelemetryKey Milestones:Infrastructure Security: Resolved all CKV_DOCKER warnings by implementing non-root users.Service Reliability: Integrated Docker Healthchecks for all microservices.Automated QA: Configured GitHub Actions for continuous vulnerability scanning.