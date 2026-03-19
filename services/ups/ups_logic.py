import paho.mqtt.client as mqtt
import time

status = "GRID_PRIMARY"
battery_level = 100.0

def on_message(client, userdata, message):
    global status, battery_level
    voltage = float(message.payload.decode())
    
    if voltage < 400:
        status = "BATTERY_DISCHARGE"
        battery_level -= 0.5
    else:
        status = "GRID_PRIMARY"
        if battery_level < 100:
            battery_level += 0.1

    print(f"[UPS] Mode: {status} | Input: {voltage}V | Battery: {round(battery_level, 1)}%")

client = mqtt.Client("UPS_System")
client.on_message = on_message
client.connect("communication_bus", 1883)
client.subscribe("dc/power/utility")
client.loop_forever()
