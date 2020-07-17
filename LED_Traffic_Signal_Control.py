import RPi.GPIO as gpio
import time

rin=3
yin=5
gin=7

gpio.setmode(gpio.BOARD)
gpio.setup(3,gpio.OUT)
gpio.setup(5,gpio.OUT)
gpio.setup(7,gpio.OUT)

while True:
    print("STOP!")
    gpio.output(3,gpio.HIGH)
    gpio.output(5,gpio.LOW)
    gpio.output(7,gpio.LOW)
    time.sleep(0.5)
    print("WAIT!")
    gpio.output(3,gpio.LOW)
    gpio.output(5,gpio.HIGH)
    gpio.output(7,gpio.LOW)
    time.sleep(0.5)
    print("GO!")
    gpio.output(3,gpio.LOW)
    gpio.output(5,gpio.LOW)
    gpio.output(7,gpio.HIGH)
    time.sleep(0.5)
    print("WAIT!")
    gpio.output(3,gpio.LOW)
    gpio.output(5,gpio.HIGH)
    gpio.output(7,gpio.LOW)
    time.sleep(0.5)
    print("STOP!")
    gpio.output(3,gpio.HIGH)
    gpio.output(5,gpio.LOW)
    gpio.output(7,gpio.LOW)
    time.sleep(0.5)
    