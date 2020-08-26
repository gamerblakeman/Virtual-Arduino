from time import sleep
from functions import *
LED_BUILTIN = 13
OUTPUT = "OUTPUT"
INPUT = "INPUT"
HIGH = True
LOW = False
render = 0
pin = 0
Serial = 0
lcd =0
def init(renderA, pinA, SerialA, lcdA, starttime):
    global render
    global pin
    global Serial
    global lcd
    lcd = lcdA
    Serial = SerialA
    render = renderA
    pin = pinA
    initsc(render, pin, starttime)

"""
DigitalReadSerial

Reads a digital input on pin 2, prints the result to the Serial Monitor

This example code is in the public domain.

http:#www.arduino.cc/en/Tutorial/DigitalReadSerial
"""
# digital pin 2 has a pushbutton attached to it. Give it a name:
pushButton = 2

# the setup routine runs once when you press reset:
def  setup() :
    # initialize serial communication at 9600 bits per second:
    Serial.begin(9600)
    # make the pushbutton's pin an input:
    pinMode(pushButton, INPUT)
    pinMode(LED_BUILTIN, INPUT)
    # set up the LCD's number of columns and rows:
    lcd.begin(16, 2)
    # Pra message to the LCD.
    lcd.print("hello, world!")
    

# the loop routine runs over and over again forever:
def  script() :
    # read the input pin:
    buttonState = digitalRead(pushButton)
    digitalWrite(LED_BUILTIN, buttonState)
    # prout the state of the button:
    lcd.setCursor(0, 1)
    lcd.print(buttonState)
    sleep(0.001)    # delay in between reads for stability
    