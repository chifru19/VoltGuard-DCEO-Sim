import paho.mqtt.client as mqtt
import time

# Use the correct arguments for Paho 2.0+
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("🛰️  EPMS Logger: Online & Monitoring dc1/roomA/ats01/source")
        client.subscribe("dc1/roomA/ats01/source")
    else:
        print(f"❌ Connection failed with code {rc}")

def on_message(client, userdata, msg):
    status = msg.payload.decode()
    log_time = time.strftime('%H:%M:%S')
    print(f"🚨 [{log_time}] DCEO EVENT: {status}")

# CRITICAL: This line tells Paho we are using the new API version
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "VoltGuard_EPMS_Logger")
client.on_connect = on_connect
client.on_message = on_message

# We know the broker is at 'localhost' because your netstat proved it!
client.connect("localhost", 1883)
client.loop_forever()