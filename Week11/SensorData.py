import RPi.GPIO as GPIO
import datetime
import board
import time
import sys
import csv


T = 0
global counts
counts = 0

runtime = int(sys.argv[1])
count_int = int(sys.argv[2])
file_name = str(sys.argv[3])+".csv"
file = open(file_name,"w", newline=None)
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
 realtime = '{}/{}/{} {}:{}:{} '.format(month, date, year, hour, minute, second)
 writer.writerow([realtime, counts])


 
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback)

while T < runtime:
 time.sleep(count_int)
 T += count_int
 print(counts)

print(counts)
print("Goodbye!")
file.close()
