import RPi.GPIO as GPIO
import datetime
import board
import time
import sys
import csv


T = 0
global counts
counts = 0

file = open("radiationdata.csv","w", newline=None)
writer = csv.writer(file)
writer.writerow(['Time', 'Counts'])

def my_callback(channel):
 
 print('\n▼  at ' + str(datetime.datetime.now()))
 print('\n ▲ at ' + str(datetime.datetime.now()))
 global counts
 counts +=1
 current_time = time.localtime()
 year = current_time[0]
 month = current_time[1]
 date = current_time[2]
 hour = current_time[3]
 minute = current_time[4]
 second = current_time[5]
 realtime = '{}/{}/{}/ {}:{}:{} '.format(month, date, year, hour, minute, second)
 writer.writerow([realtime, counts])
 time.sleep(60)


 
GPIO.setmode(GPIO.BCM)
GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


runtime = int(sys.argv[1])
while T < runtime:
 T += 60
 if T % 60 == 0:
  print(counts)

 time.sleep(60)


print(counts)
print("Goodbye!")
file.close()
