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
topicIn = "esp1in"
topicOut = "esp1out"

client = mqtt.Client("python1")

client.on_disconnect = on_disconnect
client.on_connect = on_connect
client.on_log = on_log
client.on_message = on_message

print("Connecting to broker: ", broker)
client.connect(broker)
client.loop_start()
client.subscribe(topicOut)
client.publish(topicIn, "my msg with client.py")
time.sleep(4000)
client.loop_stop()
client.disconnect()