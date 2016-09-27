import RPi.GPIO as GPIO
import time

BUTTON_TURN_UP = 27
BUTTON_TURN_DOWN = 22
SERVO_PIN = 25
ANGLE_CHANGE = 5

MIN_ANGLE = 30
MAX_ANGLE = 210 #added some tolerance from original value of 180
angle = MIN_ANGLE
first_time = True

def setup():
    global pwm
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_TURN_UP, GPIO.IN)
    GPIO.setup(BUTTON_TURN_DOWN, GPIO.IN)
    GPIO.setup(SERVO_PIN, GPIO.OUT)

    GPIO.add_event_detect(BUTTON_TURN_UP, GPIO.RISING)
    GPIO.add_event_callback(BUTTON_TURN_UP, turn_up)
    GPIO.add_event_detect(BUTTON_TURN_DOWN, GPIO.RISING)
    GPIO.add_event_callback(BUTTON_TURN_DOWN, turn_down)

    pwm = GPIO.PWM(SERVO_PIN, 100)
    pwm.start(0)

def turn_up(channel):
    global angle
    # Take away the angle change value from the current angle
    # Make sure the angle doesn't go less than minimum
    angle = angle - ANGLE_CHANGE
    if angle < MIN_ANGLE:
        angle = MIN_ANGLE
    set_angle()

def turn_down(channel):
    global angle
    # Add the delay change value to the current delay
    # Make sure the angle doesn't go greater than maximum
    angle = angle + ANGLE_CHANGE
    if angle > MAX_ANGLE:
        angle = MAX_ANGLE
    set_angle()

def set_angle():
    global angle
    global pwm
    #print "Setting angle to ", angle, " degrees"
    # -90   1.0ms
    # 0     1.5ms
    # +90   2.0ms
    duty = float(angle) / 10.0 + 2.5
    #duty = float(angle) / 10.0 + 4.5
    #print "\t with duty:", duty
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.05)
    pwm.ChangeDutyCycle(0)
    time.sleep(0.05)
    
def loop():
    global angle
    global first_time
    try:
        while True:
            if first_time is True:
                #print "first time only"
                first_time = False
                set_angle()
                time.sleep(2)
            # can be remove for manual triggering
            else:
                if angle < MAX_ANGLE:
                    done = False
                    while not done:
                        angle = angle + ANGLE_CHANGE
                        set_angle()
                        if angle > MAX_ANGLE:
                            done = True
                else:
                    done = False
                    while not done:
                        angle = angle - ANGLE_CHANGE
                        set_angle()
                        if angle < MIN_ANGLE:
                            done = True
            
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

setup()

loop()
