import RPi.GPIO as GPIO
import datetime
import board
import time
import sys

T = 0
global counts
counts = 0

def my_callback(channel):
 
 print('\n▼  at ' + str(datetime.datetime.now()))
 print('\n ▲ at ' + str(datetime.datetime.now()))
 global counts
 counts +=1


 
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback)

runtime = int(sys.argv[1])
while T < runtime:
 T += 60
 if T % 60 == 0:
  print(counts)
 time.sleep(60)


print(counts)
print("Goodbye!")
