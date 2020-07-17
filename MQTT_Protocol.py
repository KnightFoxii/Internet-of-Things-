************************************** Subscriber**********************************
import paho.mqtt.client as mymqtt
import time

#MQTT_SERVER = "test.mosquitto.org"
#MQTT_SERVER = "172.16.180.240"
MQTT_SERVER="broker.hivemq.com"
#MQTT_SERVER="iot.eclipse.org"

MQTT_TOPIC = "mit/temperature"
 
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(MQTT_TOPIC)
 
def on_message(client, userdata, msg):
    print(msg.topic+'  '+str(msg.payload))

client = mymqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, 1883, 60)
client.loop_start()
try:
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()  



***************************PUBLISHER*******************************************


#!/usr/bin/env python3
import time
import paho.mqtt.client as paho
import Adafruit_DHT as dht 

broker="broker.hivemq.com"
#broker="172.16.180.240"
#broker="iot.eclipse.org"


def on_connect(client2, userdata, flags, rc):
    print("Publisher Connected with result code "+str(rc))
    time.sleep(2)

#define DHT11 reading
def DHT11_data():
	# Sensor data of temperature and humidity
	humi, temp = dht.read_retry(11,4) 
	return humi, temp

client2= paho.Client("client-002")
print("Connecting to broker... ",broker)
client2.connect(broker)
client2.on_connect = on_connect

client2.loop_start()
try:
    while True:
	humi,temp = DHT11_data()
	print('Temperature={0:0.1f}*C  Humidity={1:0.1f}%'.format(temp, humi))
  	print("publishing... ")
	client2.publish("mit/temperature",str(temp)) 
       	time.sleep(10)
except KeyboardInterrupt:
    client2.loop_stop()
    client2.disconnect()  
		            

