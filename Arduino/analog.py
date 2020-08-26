import pygame
import sys
from pygame.locals import *
from pygame_widgets import *
import subprocess, serial
from time import sleep

class SerialEmulator(object):
    def __init__(self, device_port='./Serial/ttyAlogI', client_port='./Serial/ttyAlogO', baud=9600):
        self.device_port = device_port
        self.client_port = client_port
        cmd=['/usr/local/Cellar/socat/1.7.3.4/bin/socat','-d','-d','PTY,link=%s,raw,echo=0' % self.device_port, 'PTY,link=%s,raw,echo=0' % self.client_port]
        self.proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        sleep(1)
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

class SerialA:
    def __init__(self):
        self.serial = fakeser()
        self.outlen = self.serial.outlen()
        self.inser = ""
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
        self.old = self.inser
        self.inser = ""
        while(self.serial.available()):
            self.inser += chr(self.serial.read())
        if("@%pos" in self.inser):
            self.inser = self.old
            return(self.inser)
        else:
            return(self.inser)

    def available(self):
        return(self.serial.available())
    def begin(self, baud, pin):
        print('sersetup')
        self.serial = SerialEmulator('./Serial/ttyAlog'+pin+'i','./Serial/ttyAlog'+pin+'o', baud)
    def clear(self):
        self.serial.clear()
    
class fakeser:
    def write(self, text):
        print(text)
    def read(self):
        return(False)
    def readline(self):
        return(False)
    def available():
        return(False)
    def clear(self):
        return('0')
    def outlen(self):
        return(0)


print(str(sys.argv[1]))

Serial = SerialA() #setup serial

Serial.begin(9600, str(sys.argv[1]))

pygame.init()
win = pygame.display.set_mode((110, 70))
pygame.display.set_caption("Pin "+str(sys.argv[1]))
slider = Slider(win, 10, 10, 90, 20, min=0, max=255, step=1)
output = TextBox(win, 30, 40, 50, 30, fontSize=25)

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

    win.fill((255, 255, 255))

    slider.listen(events)
    slider.draw()

    output.setText(slider.getValue())
    Serial.clear()
    Serial.println(slider.getValue())
    output.draw()

    pygame.display.update()
    sleep(0.1)
