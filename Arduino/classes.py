#Player class
import pygame
from pygame.locals import *
white = (255,255,255)
render = 0
global screen
import os, subprocess, serial, time
def initcl(renderA, screenA):
    global render
    global screen
    render = renderA
    screen = screenA
# this script lets you emulate a serial device
# the client program should use the serial port file specifed by client_port

# if the port is a location that the user can't access (ex: /dev/ttyUSB0 often),
# sudo is required

class SerialEmulator(object):
    def __init__(self, device_port='./Serial/ttydevice', client_port='./Serial/ttyclient', baud=9600):
        self.device_port = device_port
        self.client_port = client_port
        cmd=['/usr/local/Cellar/socat/1.7.3.4/bin/socat','-d','-d','PTY,link=%s,raw,echo=0' % self.device_port, 'PTY,link=%s,raw,echo=0' % self.client_port]
        self.proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(1)
        self.serial = serial.Serial(self.device_port, baud, rtscts=True, dsrdtr=True)
        self.err = ''
        self.out = ''

    def write(self, out):
        self.serial.write(out)
    def available(self):
        if(self.serial.inWaiting() > 0):
            return(True)
        else:
            return(False)
        #1return(self.serial.inWaiting())
    def clear(self):
        self.serial.reset_output_buffer()
    def outlen(self):
        return(self.serial.out_waiting)
    
    def read(self):
        while self.serial.inWaiting() > 0:
            #print(self.serial.inWaiting())
            #line+=str(self.serial.read(1))[2]
            return(list(self.serial.read(1))[0])

        #return (line)

    def __del__(self):
        self.stop()

    def stop(self):
        self.proc.kill()
        self.out, self.err = self.proc.communicate()

#Box class



class Box:

    def __init__(self,x,y,file):
        self.x = x 
        self.y = y
        self.xm = x + 10
        self.ym = y + 10
        self.img = pygame.image.load("Arduino/resources/images/"+file+".png")
        self.rect = self.img.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.vol=0
        self.type = 'output'
        self.st = 0
        self.setA = 0

    def setsize(self):
        self.size = self.img.get_size()
        self.img = pygame.transform.scale(self.img, (int(10), int(10)))
    #self.img = pygame.transform.scale(self.img, (int(self.size[0]/4), int(self.size[1]/4)))

    def render(self):
        self.setsize()
        #screen.blit(self.img, (self.x, self.y))
        global screen
        screen.blit(self.img, [self.x,self.y])
    def rendernz(self):
        #screen.blit(self.img, (self.x, self.y))
        global screen
        screen.blit(self.img, [self.x,self.y])
        
    def chageimg(self, file):
        self.img = pygame.image.load("arduino/resources/images/"+file+".png")
    
    def voltage(self, v):
        if(v > 4.5):
            self.chageimg('5')
        elif(v == 0):
            self.chageimg('0')
        elif(v < 4.4):
            self.chageimg('3')
        
        self.vol = v
    
    
    def is_collided_with(self, sprite):
        return self.rect.colliderect(sprite.rect)

    def box(self, screen):
        pygame.draw.rect(screen, white, self.rect, 2)

    def move(self, x, y):
        self.x=x
        self.y=y
        self.rect.x=x
        self.rect.y=y

    def get_event(self, event):
        if event.type == MOUSEBUTTONUP:
            if self.hovered:
                self.callback()

class pin:
    def __init__(self):
        self.pin13 = Box(296, 30, '0')
        self.pin12 = Box(319, 30, '0')
        self.pin11 = Box(340, 30, '0')
        self.pin10 = Box(361, 30, '0')
        self.pin9 = Box(382, 30, '0')
        self.pin8 = Box(403, 30, '0')
        self.pin7 = Box(441, 30, '0')
        self.pin6 = Box(462, 30, '0')
        self.pin5 = Box(483, 30, '0')
        self.pin4 = Box(504, 30, '0')
        self.pin3 = Box(526, 30, '0')
        self.pin2 = Box(547, 30, '0')
        self.pin1 = Box(568, 30, '0')
        self.pin0 = Box(589, 30, '0')
        self.LED = Box(288, 112, '0')
        self.TX = Box(288, 153, '0')
        self.RX = Box(288, 175, '0')
        self.pinA0 = Box(483, 440, '0')
        self.pinA1 = Box(504, 440, '0')
        self.pinA2 = Box(526, 440, '0')
        self.pinA3 = Box(547, 440, '0')
        self.pinA4 = Box(568, 440, '0')
        self.pinA5 = Box(589, 440, '0')
    def render(self):
        self.LED.voltage(self.pin13.vol)
        self.pin0.render()


        self.pin1.render()

        self.pin2.render()

        self.pin3.render()

        self.pin4.render()

        self.pin5.render()

        self.pin6.render()

        self.pin7.render()

        self.pin8.render()

        self.pin9.render()

        self.pin10.render()

        self.pin11.render()

        self.pin12.render()

        self.pin13.render()
        self.LED.render()

        self.TX.render()
        self.RX.render()


        self.pinA0.render()

        self.pinA1.render()
        
        self.pinA2.render()

        self.pinA3.render()

        self.pinA4.render()

        self.pinA5.render()
    def setvol(self, pin, v):
        #print(type(pin))
        if(type(pin) == int):
            if(pin > 13):
                if(vars(self)['pinA'+str(pin -14)].type!= "dis"):
                    vars(self)['pinA'+str(pin -14)].voltage(v)
            else:
                if(vars(self)['pin'+str(pin)].type!= "dis"):
                    vars(self)['pin'+str(pin)].voltage(v)
        elif(pin.find('D') >= 0) or pin.find('d') >= 0:
            #print('digital1')
            pin = pin[1]
            #vars(self)[str(pin)].voltage(v)
            if(vars(self)['pin'+str(pin)].type!= "dis"):
                vars(self)['pin'+str(pin)].voltage(v)
        elif(pin.find('A') >= 0 or pin.find('a')>= 0):
            #print(pin[1])
            pin = pin[1]
            #vars(self)[str(pin)].voltage(v)
            if(vars(self)['pinA'+str(pin)].type!= "dis"):
                vars(self)['pinA'+str(pin)].voltage(v)
        render()
    
    def input(self, pin):
        #print(type(pin))
        print(pin)
        if(type(pin) == int):
            if(pin > 13):
                if(vars(self)['pinA'+str(pin -14)].type!= "dis"):
                    vars(self)['pinA'+str(pin -14)].chageimg('input0')
                    vars(self)['pinA'+str(pin -14)].type='input'
                    self.analogstart(pin - 14)
            else:
                if(vars(self)['pin'+str(pin)].type!= "dis"):
                    vars(self)['pin'+str(pin)].chageimg('input0')
                    vars(self)['pin'+str(pin)].type='input'
        elif("D" in pin or 'd' in pin):
            pin = pin[1]
            print(pin)
            #vars(self)[str(pin)].voltage(v)
            if(vars(self)['pin'+str(pin)].type!= "dis"):
                vars(self)['pin'+str(pin)].chageimg('input0')
                vars(self)['pin'+str(pin)].type='input'
        elif("A" in pin or 'a' in pin):
            print(pin)
            pin = pin[1]
            #vars(self)[str(pin)].voltage(v)
            if(vars(self)['pinA'+str(pin)].type!= "dis"):
                vars(self)['pinA'+str(pin)].chageimg('input0')
                vars(self)['pinA'+str(pin)].type='input'
                self.analogstart(pin)

    def output(self, pin):
        #print(type(pin))
        if(type(pin) == int):
            if(pin > 13):
                if(vars(self)['pinA'+str(pin -14)].type!= "dis"):
                    vars(self)['pinA'+str(pin -14)].chageimg('0')
                    vars(self)['pinA'+str(pin -14)].type='output'
            else:
                if(vars(self)['pin'+str(pin)].type!= "dis"):
                    vars(self)['pin'+str(pin)].chageimg('0')
                    vars(self)['pin'+str(pin)].type='output'
        elif("D" in pin or 'd' in pin):
            pin = pin[1]
            #vars(self)[str(pin)].voltage(v)
            if(vars(self)['pin'+str(pin)].type!= "dis"):
                vars(self)['pin'+str(pin)].chageimg('0')
                vars(self)['pin'+str(pin)].type='output'
        elif("A" in pin or 'a' in pin):
            pin = pin[1]
            #vars(self)[str(pin)].voltage(v)
            if(vars(self)['pinA'+str(pin)].type!= "dis"):
                vars(self)['pinA'+str(pin)].chageimg('0')
                vars(self)['pinA'+str(pin)].type='output'
    
    def changeto(self, pin, st):
        #print(type(pin))
        if(st == 1):
            if(type(pin) == int):
                if(pin > 13):
                    if(vars(self)['pinA'+str(pin-14)].type=='input'):
                        #vars(self)['pinA'+str(pin -14)].chageimg('input1')
                        #vars(self)['pinA'+str(pin -14)].st = 1
                        helpmegod = 0
                else:
                    if(vars(self)['pin'+str(pin)].type=='input'):
                        vars(self)['pin'+str(pin)].chageimg('input1')
                        vars(self)['pin'+str(pin)].st = 1

            elif("D" in pin or 'd' in pin):
                pin = pin[1]
                #vars(self)[str(pin)].voltage(v)
                if(vars(self)['pin'+str(pin)].type=='input'):
                    vars(self)['pin'+str(pin)].chageimg('input1')
                    vars(self)['pin'+str(pin)].st = 1
            elif("A" in pin or 'a' in pin):
                pin = pin[1]
                #vars(self)[str(pin)].voltage(v)
                if(vars(self)['pinA'+str(pin)].type=='input'):
                    vars(self)['pinA'+str(pin)].chageimg('input1')
                    vars(self)['pinA'+str(pin)].st = 1
        elif(st == 0):
            if(type(pin) == int):
                if(pin > 13):
                    if(vars(self)['pinA'+str(pin-14)].type=='input'):
                        helpmegod = 0
                        #vars(self)['pinA'+str(pin -14)].chageimg('input0')
                        #vars(self)['pinA'+str(pin -14)].st = 0
                else:
                    if(vars(self)['pin'+str(pin)].type=='input'):
                        vars(self)['pin'+str(pin)].chageimg('input0')
                        vars(self)['pin'+str(pin)].st = 0
            elif("D" in pin or 'd' in pin):
                pin = pin[1]
                #vars(self)[str(pin)].voltage(v)
                if(vars(self)['pin'+str(pin)].type=='input'):
                    vars(self)['pin'+str(pin)].chageimg('input0')
                    vars(self)['pin'+str(pin)].st = 0
            elif("A" in pin or 'a' in pin):
                pin = pin[1]
                #vars(self)[str(pin)].voltage(v)
                if(vars(self)['pinA'+str(pin)].type=='input'):
                    vars(self)['pinA'+str(pin)].chageimg('input0')
                    vars(self)['pin'+str(pin)].st = 0
        render()
    def disable(self, array):
        for pin in array:
            vars(self)['pin'+str(pin)].chageimg('input0')
            vars(self)['pin'+str(pin)].type = "dis"
    def analogstart(self, pin):
        
        self.args = ["/usr/local/opt/python@3.8/bin/python3.8", "/Users/james/Desktop/Virtal Rarduino/Arduino/analog.py", pin]
        vars(self)['procA'+str(pin)] = subprocess.Popen(self.args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        time.sleep(4)
        s_name = './Serial/ttyAlog'+pin+'o'
        vars(self)['serA'+str(pin)] = serial.Serial(s_name)
    def analogread(self, pin):
        vars(self)['ser'+str(pin)].flushInput()
        return(vars(self)['ser'+str(pin)].readline())




class SerialA:
    def __init__(self):
        self.serial = fakeser()
        self.outlen = self.serial.outlen()
    def print(self, text):
        self.outlen = self.serial.outlen()
        print(text)
        text = str(text)
        text = str.encode(text)
        self.serial.write(text)
    def println(self, text):
        self.outlen = self.serial.outlen()
        text = str(text)
        text = str.encode(text+'\n')
        self.serial.write(text)
    def read(self, A):
        return(self.serial.read())
    def available(self):
        return(self.serial.available())
    def begin(self, baud):
        print('sersetup')
        self.serial = SerialEmulator('./Serial/ttydevice','./Serial/ttyclient', baud)
    def clear(self):
        self.serial.clear()
    
class fakeser:
    def write(self, text):
        print(text)
    def read(self):
        return(False)
    def available():
        return(False)
    def clear(self):
        return('0')
    def outlen(self):
        return(0)
class lcdC:
    def __init__(self):
        self.init = 1
    def begin(self, l, h):
        self.args = ["/usr/local/opt/python@3.8/bin/python3.8", "/Users/james/Desktop/Virtal Rarduino/Arduino/LCD.py"]
        self.child_proccess = subprocess.Popen(self.args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        time.sleep(4)
        s_name = './Serial/ttylcdo'
        self.ser = serial.Serial(s_name)
    def setCursor(self, x, y):
        self.posX = x
        self.posY = y
        text = str('@%pos'+str(x)+','+str(y)+'\n')
        text = str.encode(text)
        self.ser.write(text)
        time.sleep(0.1)
    def print(self, text):
        text = str(text)
        text = str.encode(text)
        self.ser.write(text)
        self.text = text
