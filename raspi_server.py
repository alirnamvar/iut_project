import time
from mqtt import MQTT

def main():
    client = MQTT("localhost", 1883, 'raspi')
    client.connect()
    counter = 0
    # client.publish("inventory/assembly", str(send))
    while True:
        # infot = client.publish("inventory/assembly", str(send))
        # infot.wait_for_publish()
        if counter == 3:
            client.publish("inventory/order", '0201')
        # print(f"MQTTMessageInfo: {pub_reterned}")
        counter += 1
        # print('Wait 3 seconds')
        time.sleep(3)

if __name__ == '__main__':
    main()