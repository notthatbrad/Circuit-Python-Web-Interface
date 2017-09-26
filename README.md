# Circuit Python Web Interface

This is a basic websockets interface for communicating with the webrepl on a device running Circuit Python.

The purpose of this project is to demonstrate using websockets to create a connection to the webrepl to manipulate GPIO pins. This is just a simple demonstraton. Once the websocket is open, any valid Circuit Python code can be sent and executed just as it would be in the repl or webrepl interface.

Webrepl must be enabled on your device for this to function. If it is not, instructions can be found here https://learn.adafruit.com/micropython-basics-esp8266-webrepl/access-webrepl .


FILES
main.py-this should be uploaded to the main directoryy on the ESP8266, it contains the code for pin manipulation, and will run at boot.
index.html-this file contains the html that will be run in your web browser.

USE The default code uses pin 4. Pin 5 is also available in the demo to demonstrate how to switch pin input. 

There are many ways to detect the state of the pin, but an led and 470 ohm resistor is what I have been using.
