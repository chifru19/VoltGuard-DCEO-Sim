import paho.mqtt.client as mqtt
import os
import time
from paho.mqtt.enums import CallbackAPIVersion

# 1. Configuration
BROKER_ADDRESS = os.getenv("MQTT_BROKER", "mqtt-broker")

# 2. Logic Callback
def on_message(client, userdata, message):
    load = float(message.payload.decode())
    # If load is over 75, UPS kicks in
    status = "UPS_ACTIVE" if load > 75 else "UTILITY_OK"
    client.publish("voltguard/ups/status", status)
    print(f"Inbound Load: {load} | System Status: {status}")

# 3. Client Setup
client = mqtt.Client(CallbackAPIVersion.VERSION1, "UPSLogic")
client.on_message = on_message

# 4. Connection Loop
while True:
    try:
        client.connect(BROKER_ADDRESS, 1883)
        print(f"UPS Logic connected to {BROKER_ADDRESS}")
        break
    except:
        time.sleep(2)

# 5. Subscribe and Wait
client.subscribe("voltguard/utility/load")
client.loop_forever()