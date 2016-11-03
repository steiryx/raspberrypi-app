import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BCM)
 
Motor1P = 23    # Input Pin
Motor1N = 24    # Input Pin
TriggerA = 25    # Enable Pin

GPIO.setup(Motor1P,GPIO.OUT)
GPIO.setup(Motor1N,GPIO.OUT)
GPIO.setup(TriggerA, GPIO.OUT)
 
Motor2P = 27    # Input Pin
Motor2N = 17   # Input Pin
TriggerB = 22    # Enable Pin

GPIO.setup(Motor2P,GPIO.OUT)
GPIO.setup(Motor2N,GPIO.OUT)
GPIO.setup(TriggerB, GPIO.OUT)
 
print "FORWARD MOTION1"
GPIO.output(TriggerA,GPIO.HIGH)
GPIO.output(Motor1P,GPIO.HIGH)
GPIO.output(Motor1N,GPIO.LOW)
print "FORWARD MOTION2"
GPIO.output(TriggerB,GPIO.HIGH)
GPIO.output(Motor2P,GPIO.HIGH)
GPIO.output(Motor2N,GPIO.LOW)

sleep(15)
 
print "BACKWARD MOTION"
GPIO.output(TriggerA,GPIO.HIGH)
GPIO.output(Motor1P,GPIO.LOW)
GPIO.output(Motor1N,GPIO.HIGH)
 
GPIO.output(TriggerB,GPIO.HIGH)
GPIO.output(Motor2P,GPIO.LOW)
GPIO.output(Motor2N,GPIO.HIGH)

sleep(15)
 
print "STOP"
GPIO.output(TriggerA,GPIO.LOW)
GPIO.output(TriggerB,GPIO.LOW)
 
GPIO.cleanup()
