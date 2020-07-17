import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.OUT)
TRIG = 11
ECHO = 7
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG,False)
print "Calibrating...."
time.sleep(2)
print "Place the object.."
try:    
    while True:
        
        GPIO.output(TRIG,True)
        time.sleep(0.00001)
        
       # print "1"
        GPIO.output(TRIG,False)
        #print "2"
        
        while GPIO.input(ECHO)==0:
            pulse_start = time.time()
          #  print "4"
        
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()
           # print "5"   
        pulse_duration = pulse_end - pulse_start
    
        distance = pulse_duration * 17150
    
        distance =  round(distance+1.1,2)
        
        if distance>20:
            print "Distance:",distance,"cm"
            print "lai jhakkkkkk lamach raha atta kalle ka ????"
            GPIO.output(13,GPIO.HIGH)
        else:
            print("LAI JAVAL AHE BABA TUMHI LAMB JAA , NEED SOME SPACE ")
            GPIO.output(13,GPIO.LOW)
        time.sleep(2)
    
except KeyboardInterrupt:
    GPIO.cleanup()
