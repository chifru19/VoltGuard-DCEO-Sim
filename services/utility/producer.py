import paho.mqtt.client as mqtt
import time
import random
import os

# Get connection details from environment variables
MQTT_BROKER = os.getenv("MQTT_BROKER", "mqtt-service")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))

client = mqtt.Client()

print(f"--- Starting Utility Producer ---", flush=True)
print(f"Connecting to: {MQTT_BROKER} on port {MQTT_PORT}", flush=True)

# Loop until successfully connected
while True:
    try:
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        print("✅ SUCCESS: Connected to MQTT Broker!", flush=True)
        break
    except Exception as e:
        print(f"❌ Connection failed: {e}. Retrying in 2s...", flush=True)
        time.sleep(2)

# Main loop to send data
while True:
    load = random.randint(20, 90)
    client.publish("voltguard/utility/load", str(load))
    print(f"🚀 Sent Load Data: {load}%", flush=True)
    time.sleep(5)