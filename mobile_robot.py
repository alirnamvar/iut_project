import time
from mqtt import MQTT

def main():
    client = MQTT("localhost", 1883, 'mobile')
    client.connect()
    client.loop_start()
    client.subscribe("inventory/order")
    print("Listening in 'inventory/order' topic...")

    while True:
        # pub_reterned = client.publish("inventory/assembly", str(send))
        # print(f"MQTTMessageInfo: {pub_reterned}")

        if client.get_recived_message() is not None:
            reviced_reder = client.get_recived_message()
            # process_order(reviced_reder)
            client.set_recived_message_None()

        time.sleep(1)

def process_order(order):
    print(f"Processing order: {order}")

if __name__ == '__main__':
    main()
