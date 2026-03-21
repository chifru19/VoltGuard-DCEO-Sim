import paho.mqtt.client as mqtt
import os
import json

# Configuration from Environment Variables
MQTT_BROKER = os.getenv("MQTT_BROKER", "mqtt-service")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))

def on_connect(client, userdata, flags, rc):
    print(f"Connected to broker with result code {rc}")
    client.subscribe("voltguard/utility/load")

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload)
        load = data.get("load", 0)
        
        # Resiliency Logic: Switch to UPS if load exceeds 75%
        status = "UPS_ACTIVE" if load > 75 else "UTILITY_OK"
        
        print(f"Published Load: {load}% | System Status: {status}")
        client.publish("voltguard/ups/status", json.dumps({"status": status, "load": load}))
    except Exception as e:
        print(f"Error processing message: {e}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)
