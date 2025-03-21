import RPi.GPIO as GPIO
import datetime
 
def my_callback(channel):
    
    if GPIO.input(channel) == GPIO.HIGH:
        print('\n▼  at ' + str(datetime.datetime.now()))
    else:
        print('\n ▲ at ' + str(datetime.datetime.now()))

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(17, GPIO.BOTH, callback=my_callback)
    message = raw_input('\nPress any key to exit.\n')

#answer = my_callback(17)
#print(answer)

finally:
    GPIO.cleanup()
 
print("Goodbye!")
