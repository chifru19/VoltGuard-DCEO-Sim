import os
import paho.mqtt.client as mqtt

BROKER = os.getenv("MQTT_BROKER", "mqtt-broker")
PORT = 1883
LOG_FILE = "incident_audit_log.txt"

def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT broker with result code {rc}")
    client.subscribe("voltguard/#")

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    log_entry = f"Topic: {msg.topic} | Message: {payload}\n"
    print(log_entry.strip())
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)

def main():
    try:
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "EPMS_Logger")
    except AttributeError:
        client = mqtt.Client("EPMS_Logger")
        
    client.on_connect = on_connect
    client.on_message = on_message
    
    print(f"Connecting EPMS Logger to: {BROKER} on port {PORT}")
    client.connect(BROKER, PORT, 60)
    client.loop_forever()

if __name__ == "__main__":
    main()
