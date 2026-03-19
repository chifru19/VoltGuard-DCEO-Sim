import paho.mqtt.client as mqtt
import time
import random

# Connection details for our virtual SCADA network
BROKER = "communication_bus" 
PORT = 1883
TOPIC = "dc/power/utility"

client = mqtt.Client("Utility_Provider")

def connect_to_broker():
    while True:
        try:
            client.connect(BROKER, PORT)
            print("Connected to Communication Bus")
            break
        except:
            print("Waiting for bus...")
            time.sleep(2)

connect_to_broker()

while True:
    # Normally, we want ~480V for a commercial feed
    # We add a bit of 'noise' to make it realistic
    voltage = round(random.uniform(478.0, 482.0), 2)
    
    # SIMULATE A GRID FAILURE: 
    # Every 45 seconds, drop voltage to 0 to test the UPS
    if int(time.time()) % 45 == 0:
        voltage = 0.0
        print("!!! GRID FAILURE DETECTED !!!")
    
    client.publish(TOPIC, voltage)
    print(f"Utility Output: {voltage}V")
    time.sleep(1)