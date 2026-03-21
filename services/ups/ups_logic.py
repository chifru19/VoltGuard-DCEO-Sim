import paho.mqtt.client as mqtt
import os
import time
from paho.mqtt.enums import CallbackAPIVersion

# 1. Configuration
BROKER_ADDRESS = os.getenv("MQTT_BROKER", "mqtt-service")

# 2. Logic Callback
def on_message(client, userdata, message):
    load = float(message.payload.decode())
    # If load is over 75, UPS kicks in
    status = "UPS_ACTIVE" if load > 75 else "UTILITY_OK"
    client.publish("voltguard/ups/status", status)
    print(f"Inbound Load: {load} | System Status: {status}")

# 3. Client Setup
client = mqtt.Client(CallbackAPIVersion.VERSION2, "UPSLogic")
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
# Constants for DCEO Thresholds
WARNING_THRESHOLD = 80.0
CRITICAL_THRESHOLD = 95.0

def process_telemetry(payload):
    load = payload.get("load_kw", 0)
    
    if load >= CRITICAL_THRESHOLD:
        print(f"🛑 [CRITICAL ALARM] Load at {load}%! Triggering UPS Failover...")
        # In a real AWS site, this would start the Generators
        publish_alert("FAILOVER_ACTIVE")
        
    elif load >= WARNING_THRESHOLD:
        print(f"⚠️ [WARNING] Load at {load}%. DCEO investigation required.")
        publish_alert("LOAD_INVESTIGATION")
        
    else:
        print(f"✅ [NORMAL] Load at {load}%. Infrastructure stable.")