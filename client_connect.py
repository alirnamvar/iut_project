import paho.mqtt.client as mqtt
import time

def on_log(client, userdata, level, buf):
    print("log: ",buf)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connection is Ok.")
    else:
        print("Bad connection. Returned code=", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected and Resualt code:", rc)


def on_message(client, userdata, msg):
    topic = msg.topic
    m_decode = str(msg.payload.decode('utf-8'))
    print(f"message recived: {m_decode}")


broker = "172.24.97.253"
client = mqtt.Client('raspi')
# client.on_log = on_log
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

print('Connecting to broker: ', broker)
client.connect(broker, 1883)

### starting loop
client.loop_start()

client.subscribe("inventory/assembly")
client.publish("inventory/assembly", "first message")
time.sleep(4)

### stoping loop
client.loop_stop()

client.disconnect()