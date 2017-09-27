from machine import Pin

#initialize data to defaults
startD = "|~~|"
endD= "~||~"
ledPin = Pin(4, Pin.OUT)    # create output pin on GPIO0

#function for toggling the pin on and off
def toggle():
	ledPin.value(not ledPin.value())
	print('%sToggled%s' % (startD, endD))

#function for turning on the pin
def turnOn():
	ledPin.on() 
	print('%sTurned On%s' % (startD, endD))

#function for turning off the pin
def turnOff():
	ledPin.off() 
	print('%sTurned Off%s' % (startD, endD))

	
#to set custom delimiters. If not called, the default values will be used
def setDelimiters(dStart, dEnd):
	global startD
	startD = dStart
	global endD
	endD = dEnd
	print("%sConnected and ready for input.%s" % (startD, endD))
	
def changePinNumber(pNumber):
	global ledPin
	temp = ledPin.value()
	ledPin.off()
	ledPin = Pin(pNumber, Pin.OUT)
	ledPin.value(temp)
	print('%snow using pin %s %s' % (startD, pNumber, endD))