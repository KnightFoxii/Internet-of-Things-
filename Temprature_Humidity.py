import Adafruit_DHT
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

sensor=Adafruit_DHT.DHT11
 

gpio=17
 

humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
 
if(temperature > 25 and humidity > 85):
 if humidity is not None and temperature is not None:
  print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
  print("LED ON!")
  GPIO.output(18,GPIO.HIGH)
 else:
  print('Failed to get reading. Try again!')

else:
  if humidity is not None and temperature is not None:
   print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
   print("LED OFF")
   GPIO.output(18,GPIO.LOW)
  else:
   print('Failed to get reading. Try again!')






