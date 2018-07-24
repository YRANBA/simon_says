import RPi.GPIO as GPIO
import LEDRGB as LED
import time
import random

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

buzz_pin = 32

GPIO.setup(buzz_pin,GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin, 1000)


colors = [ 'R' ,  'G',  'B' ,  'Y'] 
R_pin = 11
G_pin = 12
B_pin  = 13 
frequencies = [220, 440, 880, 1760]
previous = []
LED.setup(R_pin, G_pin, B_pin)
def append_list ( ):
		while True:
				n =random.randint (0,3)
				previous.append(n)
				for i in previous:
					LED.setColor (colors[i])
					Buzz.ChangeFrequency(frequencies[i])
					Buzz.start(25)
					time.sleep(1)
					Buzz.stop( )
					LED.noColor( )
					time.sleep(1)

if __name__ == '__main__' :
		try:
				append_list ( )
		except KeyboardInterrupt:
				print "goodbye"
				LED.destroy( )
				Buzz.stop( )

