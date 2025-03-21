import RPi.GPIO as GPIO
import datetime
import board
import time

T = 0

def my_callback(channel):
 print('\n▼  at ' + str(datetime.datetime.now()))
 print('\n ▲ at ' + str(datetime.datetime.now()))
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(11, GPIO.FALLING, callback=my_callback)

runtime = int(sys.argv[1])
while T < runtime:
 T += 10
 time.sleep(10)

 
print("Goodbye!")
