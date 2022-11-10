import time
from mqtt import MQTT

def main():
    client = MQTT("localhost", 1883, 'moob')
    client.connect()
    counter = 0
    # client.publish("inventory/assembly", str(send))
    # infot = client.publish("inventory/assembly", str(send))
    # infot.wait_for_publish()
    client.publish("inventory/rawMaterialsPosition", '10#20')

if __name__ == '__main__':
    main()