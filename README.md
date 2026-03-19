# VoltGuard-DCEO-Sim

A containerized simulation of a Data Center Energy Optimization (DCEO) system. This project simulates a power grid utility feed and a UPS (Uninterruptible Power Supply) logic that monitors load levels via MQTT.

## Architecture
- **MQTT Broker**: Eclipse Mosquitto (The central message hub)
- **Utility Feed**: Simulates real-time power grid load data.
- **UPS System**: Intelligent logic that triggers battery backup during high load.
- **Monitoring Station**: Logs all system traffic for analysis.

## How to Run
1. Ensure you have Docker Desktop installed.
2. Clone the repository.
3. Run the following command:
   ```bash
   docker-compose up --build