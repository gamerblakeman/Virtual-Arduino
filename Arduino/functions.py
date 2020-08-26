import datetime
render = 0
pin = 0
starttime = 0
def initsc(renderA, pinA, starttimeA):
    global render
    global pin
    global starttime
    render = renderA
    pin = pinA
    starttime= starttimeA

def digitalRead(pinno):
    global pin
    if(pinno > 13):
        return(bool(vars(pin)['pinA'+str(pinno-14)].st))
    else:
        return(bool(vars(pin)['pin'+str(pinno)].st))

def pinMode(pinno, mode):
    global pin
    if(mode == "INPUT"):
        pin.input(pinno)
    else:
        pin.output(pinno)
def digitalWrite(pinno, mode):
    global render
    global pin
    if(mode == True):
        pin.setvol(pinno, 5)
    elif(mode == False):
        pin.setvol(pinno, 0)
def analogWrite(pinno, mode):
    global render
    global pin
    pin.setvol(pinno, mode/51)
def millis():
    return(datetime.datetime.now() - starttime)
def analogRead(pinA):
    return(int(pin.analogread(pinA)))
