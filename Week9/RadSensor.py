import RPi.GPIO as GPIO
import datetime
import board
import time
import sys

def my_callback(channel):
 
  if print('\n▼  at ' + str(datetime.datetime.now())) == True:
   counts += 1
  if print('\n ▲ at ' + str(datetime.datetime.now())) == True:
   counts += 1
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback)

runtime = int(sys.argv[1])
while T < runtime:
 T += 10
 time.sleep(10)

 
print("Goodbye!")
