import paho.mqtt.client as mqtt
import time
import random
import os
from paho.mqtt.enums import CallbackAPIVersion

# 1. Configuration
# We use the internal Kubernetes Service name 'mqtt-service'
BROKER_ADDRESS = os.getenv("MQTT_BROKER", "mqtt-service")
MQTT_PORT = 1883
TOPIC = "voltguard/utility/load"

# 2. Initialization
# Using Version 2 of the Callback API to ensure compatibility with modern Paho-MQTT
client = mqtt.Client(CallbackAPIVersion.VERSION2, "UtilityFeed")

# 3. Persistent Connection Loop
while True:
    try:
        client.connect(BROKER_ADDRESS, MQTT_PORT)
        print(f"✅ Utility Producer successfully connected to {BROKER_ADDRESS}")
        break
    except Exception as e:
        print(f"❌ Connection failed: {e}. Retrying in 2 seconds...")
        time.sleep(2)

# 4. Telemetry Generation Loop
print("🚀 Telemetry stream initiated...")
while True:
    # --- STEADY STATE MODE ---
    # Generates a random load between 20.0 and 90.0
    load = round(random.uniform(20.0, 90.0), 2)
    
    # --- STRESS TEST MODE ---
    # Uncomment the line below to force a critical alarm state (UPS_ACTIVE)
    # load = 95.5
    
    # Dispatch payload
    result = client.publish(TOPIC, load)
    
    if result.rc == mqtt.MQTT_ERR_SUCCESS:
        print(f"📊 Published Load: {load}%")
    else:
        print("⚠️ Failed to publish data packet.")

    # Data frequency: 5-second intervals
    time.sleep(5)