import RPi.GPIO as GPIO
import datetime
import board
import time
import sys

T = 0

def my_callback(channel):
 counts = 0
 print('\n▼  at ' + str(datetime.datetime.now()))
 if print('\n▼  at ' + str(datetime.datetime.now())) == True:
  counts += 1
 print('\n ▲ at ' + str(datetime.datetime.now()))
 if print('\n ▲ at ' + str(datetime.datetime.now())) == True:
  counts += 1
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback)

runtime = int(sys.argv[1])
while T < runtime:
 T += 10
 time.sleep(10)

print(counts)
print("Goodbye!")
