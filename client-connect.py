import paho.mqtt.client as mqtt
import time

def on_log(client, userdata, level, buf):
    print("log: ", buf)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Success on connecting!")
    else:
        print("Connection refused with code: ", rc)

def on_disconnect(client, userdata, flags, rc = 0):
    print("Disconnected result code: ", str())

def on_message(client, userdata, msg):
    topic = msg.topic
    m_decode = str(msg.payload.decode("utf-8"))
    print("Message received: ", m_decode)

broker = "35.193.185.214"
topicIn = "esp1Led1Topic"
topicOut = "esp1TempTopic"

client = mqtt.Client("python1")

client.on_disconnect = on_disconnect
client.on_connect = on_connect
client.on_log = on_log
client.on_message = on_message

option = input("Select the option: ")

print("Connecting to broker: ", broker)
client.connect(broker)
client.loop_start()
time.sleep(1)

if option == 'p':
    while True: 
        sendAmount = input("Select the brightness to send to the led: (0-1024) ")
        client.publish(topicIn, "b{}".format(sendAmount))
elif option == 's':
    client.subscribe(topicOut)
    
time.sleep(4000)
client.loop_stop()
client.disconnect()