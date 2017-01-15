try:
	import RPi.GPIO as GPIO
except ImportError:
    raise ImportError("You must use this on a raspberry pi for the GPIO library to be initialized!")

class Relay:

    def __init__(self, port):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(port, GPIO.OUT)
		GPIO.output(port, False)
		self.port = port
       
    def go(self, value):
		if (value == "on"):
			GPIO.output(self.port, True)
		else:
			GPIO.output(self.port, False)
		
    def __del__(self):
		GPIO.cleanup()


