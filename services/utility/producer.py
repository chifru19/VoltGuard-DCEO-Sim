import paho.mqtt.client as mqtt
import time
import random
import os
from paho.mqtt.enums import CallbackAPIVersion

# 1. Configuration
BROKER_ADDRESS = os.getenv("MQTT_BROKER", "mqtt-broker")

# 2. Client Setup
client = mqtt.Client(CallbackAPIVersion.VERSION1, "UtilityFeed")

# 3. Connection Loop
while True:
    try:
        client.connect(BROKER_ADDRESS, 1883)
        print(f"Utility connected to {BROKER_ADDRESS}")
        break
    except:
        time.sleep(2)

# 4. Data Generation Loop
while True:
    load = round(random.uniform(20.0, 90.0), 2)
    client.publish("voltguard/utility/load", load)
    print(f"Sent Utility Load: {load}")
    time.sleep(5)