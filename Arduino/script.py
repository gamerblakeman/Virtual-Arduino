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
A0, A1, A2, A3, A4, A5 = "A0","A1","A2","A3","A4","A5"

rs, en, d4, d5, d6, d7 = 12,  11,  5,  4,  3,  2

analogPin = A3
val = 0

def  setup() :
    pin.disable([rs, en, d4, d5, d6, d7]) 
    # put your setup code here, to run once:
    lcd.begin(16, 2)
    # Pra message to the LCD.
    lcd.print("hello, world!")
    Serial.begin(9600)
    Serial.println("hello")
    pinMode(A1, INPUT)
    pinMode(6, INPUT)
    pinMode(A0, INPUT)
    pinMode(7, INPUT)
    lcd.clear()
    

def  script() :
    # put your main code here, to run repeatedly:
    lcd.clear()
    lcd.setCursor(0, 0)
    val = analogRead(A1)  # read the input pin
    analogWrite(6,val)
    lcd.print(val)
    lcd.setCursor(1, 0)
    val = analogRead(A0)  # read the input pin
    analogWrite(7,val)
    lcd.print(val)
    sleep(0.2)
    
    
