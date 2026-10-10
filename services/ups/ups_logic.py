import os
import paho.mqtt.client as mqtt

BROKER = os.getenv("MQTT_BROKER", "mqtt-broker")
PORT = 1883

def on_connect(client, userdata, flags, rc):
    print(f"UPS Connected to broker with code {rc}")
    client.subscribe("voltguard/utility/load")

def on_message(client, userdata, msg):
    try:
        load = float(msg.payload.decode())
        print(f"UPS received load: {load}%")
        if load > 80.0:
            print("⚠️ ALERT: Load > 80%! Switching to BATTERY_MODE")
            client.publish("voltguard/ups/status", "BATTERY_MODE")
        else:
            client.publish("voltguard/ups/status", "NORMAL")
    except ValueError:
        pass

def main():
    try:
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "UPS_Unit")
    except AttributeError:
        client = mqtt.Client("UPS_Unit")
        
    client.on_connect = on_connect
    client.on_message = on_message
    
    print(f"Connecting UPS Logic to: {BROKER} on port {PORT}")
    client.connect(BROKER, PORT, 60)
    client.loop_forever()

if __name__ == "__main__":
    main()
