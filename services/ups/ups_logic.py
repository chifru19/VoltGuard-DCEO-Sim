import paho.mqtt.client as mqtt
client = mqtt.Client("UPS_Unit")
def on_message(c, u, m):
    v = float(m.payload.decode())
    status = "BATTERY MODE" if v < 100 else "GRID ONLINE"
    print(f"UPS Status: {status} ({v}V)")
client.on_connect = lambda c,u,f,rc: client.subscribe("dc/power/utility")
client.on_message = on_message
client.connect("communication_bus", 1883)
client.loop_forever()
