import time
from mqtt import MQTT
import argparse

def main():
    #my_parser = argparse.ArgumentParser()
    #my_parser.add_argument('--input', action='store', type=int, required=True)
    client = MQTT("localhost", 1883, 'plc')
    client.connect()
    #send = my_parser.parse_args().input
    # client.publish("inventory/assembly", str(send))

    # infot = client.publish("inventory/assembly", str(send))
    # infot.wait_for_publish()
    # while True:
    client.publish("warehouse/palletRecived", "yes")

if __name__ == '__main__':
    main()
