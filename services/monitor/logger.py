import paho.mqtt.client as mqtt
import os
import time
from paho.mqtt.enums import CallbackAPIVersion

# 1. Configuration
BROKER_ADDRESS = os.getenv("MQTT_BROKER", "mqtt-broker")

# 2. Callback function
def on_message(client, userdata, message):
    print(f"[MONITOR] {message.topic}: {message.payload.decode()}")

# 3. Client Setup (using the correct API version)
client = mqtt.Client(CallbackAPIVersion.VERSION1, "MonitoringStation")
client.on_message = on_message

# 4. Connection Loop
while True:
    try:
        print(f"Monitor connecting to {BROKER_ADDRESS}...")
        client.connect(BROKER_ADDRESS, 1883)
        break
    except Exception as e:
        print(f"Waiting for broker... {e}")
        time.sleep(2)

# 5. Start Listening
client.subscribe("voltguard/#")
print("Monitoring all 'voltguard/#' topics...")
client.loop_forever()