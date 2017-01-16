try:
	import RPi.GPIO as GPIO
except ImportError:
	raise ImportError("You must use this on a raspberry pi for the GPIO library to be initialized!")

class Relay:

	def __init__(self, port, inverse):
		self.inverse = inverse
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(port, GPIO.OUT)
		GPIO.output(port, inverse)

		self.port = port
	   
	def go(self, value):
		if (value == "on"):
			GPIO.output(self.port, not self.inverse)
		else:
			GPIO.output(self.port, self.inverse)
		
