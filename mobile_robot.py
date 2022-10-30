import time
from mqtt import MQTT

def main():
    client = MQTT("localhost", 1883, 'mobile_robot')
    client.connect()
    client.loop_start()
    client.subscribe("inventory/order")

    while True:
        # pub_reterned = client.publish("inventory/assembly", str(send))
        # print(f"MQTTMessageInfo: {pub_reterned}")

        if client.get_recived_message() is not None:
            print(client.get_recived_message())
            client.set_recived_message_None()

        time.sleep(3)

if __name__ == '__main__':
    main()