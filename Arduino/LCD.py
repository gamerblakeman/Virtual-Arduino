# 1 - Import library
import pygame
import subprocess, serial
from pygame.locals import *
from time import sleep
from colour import Color


class lcdclass:
    def __init__(self):
        self.screen2Y = 110
        self.screen2X = 490
        self.posX = 0
        self.posY = 0
    def begin(self, colorIN):
        self.screen2=pygame.display.set_mode((self.screen2X, self.screen2Y))
        self.toprow()
        self.botomrow()
        self.color = colorIN
        self.rgb = Color(self.color).rgb
        self.rgb = [self.rgb[0]* 255, self.rgb[1]* 255, self.rgb[2]* 255]
    def render(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit() 
                exit(0)
        self.screen2.fill(self.rgb) 
        self.T1.render(self)
        self.T2.render(self)
        self.T3.render(self)
        self.T4.render(self)
        self.T5.render(self)
        self.T6.render(self)
        self.T7.render(self)
        self.T8.render(self)
        self.T9.render(self)
        self.T10.render(self)
        self.T11.render(self)
        self.T12.render(self)
        self.T13.render(self)
        self.T14.render(self)
        self.T15.render(self)
        self.T16.render(self)
        self.B1.render(self)
        self.B2.render(self)
        self.B3.render(self)
        self.B4.render(self)
        self.B5.render(self)
        self.B6.render(self)
        self.B7.render(self)
        self.B8.render(self)
        self.B9.render(self)
        self.B10.render(self)
        self.B11.render(self)
        self.B12.render(self)
        self.B13.render(self)
        self.B14.render(self)
        self.B15.render(self)
        self.B16.render(self)
        pygame.display.set_caption("LCD")
        pygame.display.flip()
        
    def toprow(self):
        self.T1 = Box(10,10, 'input0')
        self.T2 = Box(40,10, 'input0')
        self.T3 = Box(70,10, 'input0')
        self.T4 = Box(100,10, 'input0')
        self.T5 = Box(130,10, 'input0')
        self.T6 = Box(160,10, 'input0')
        self.T7 = Box(190,10, 'input0')
        self.T8 = Box(220,10, 'input0')
        self.T9 = Box(250,10, 'input0')
        self.T10 = Box(280,10, 'input0')
        self.T11 = Box(310,10, 'input0')
        self.T12 = Box(340,10, 'input0')
        self.T13 = Box(370,10, 'input0')
        self.T14 = Box(400,10, 'input0')
        self.T15 = Box(430,10, 'input0')
        self.T16 = Box(460,10, 'input0')
    def botomrow(self):
        self.B1 = Box(10,60, 'input0')
        self.B2 = Box(40,60, 'input0')
        self.B3 = Box(70,60, 'input0')
        self.B4 = Box(100,60, 'input0')
        self.B5 = Box(130,60, 'input0')
        self.B6 = Box(160,60, 'input0')
        self.B7 = Box(190,60, 'input0')
        self.B8 = Box(220,60, 'input0')
        self.B9 = Box(250,60, 'input0')
        self.B10 = Box(280,60, 'input0')
        self.B11 = Box(310,60, 'input0')
        self.B12 = Box(340,60, 'input0')
        self.B13 = Box(370,60, 'input0')
        self.B14 = Box(400,60, 'input0')
        self.B15 = Box(430,60, 'input0')
        self.B16 = Box(460,60, 'input0')
    def clear(self):
        self.posX = 0
        self.posY = 0
        self.write("                                          ")
        self.posX = 0
        self.posY = 0
    def setpos(self, x, y):
        self.x = y
        self.y = x

    def write(self, text):
        self.font = pygame.font.Font('freesansbold.ttf', 25) 
        # create a text suface object, 
        # on which text is drawn on it. 
        i = self.posX + 1
        if(self.posY == 0):
            a = "T"
        else:
            a = "B"
        for char in text:
            self.posX = i
            if(a == "T"):
                self.posY = 0
            else:
                self.posY = 1
            if(i <= 16):
                vars(self)[str(a)+str(i)].addtext(char, self.font)
                #print(char)
                i = i + 1
            elif(a != "B"):
                a = "B"
                i = 1
                #print(char)
                vars(self)[str(a)+str(i)].addtext(char, self.font)
                i = i + 1
        


class Box:

    def __init__(self,x,y,file):
        self.x = x 
        self.y = y
        self.xm = x + 10
        self.ym = y + 10
        self.img = pygame.image.load("Arduino/resources/images/"+file+".png")
        self.rect = self.img.get_rect()
        self.font = pygame.font.Font('freesansbold.ttf', 25) 
        self.text = self.font.render(' ', True, [255,255,255]) 

    def setsize(self):
        self.size = self.img.get_size()
        self.img = pygame.transform.scale(self.img, (int(20), int(40)))

    def render(self, lcd):
        
        self.setsize()
        self.img.set_alpha(100)
        #screen2.blit(self.img, (self.x, self.y)
        self.rect = self.img.get_rect()
        #self.rect.center = (40, 10)
        self.rect.top = self.y
        self.rect.left = self.x
        #[self.x,self.y]
        lcd.screen2.blit(self.img, self.rect)
        lcd.screen2.blit(self.text, [self.x, self.y+8]) 
    def rendernz(self):
        #screen2.blit(self.img, (self.x, self.y))
        lcd.screen2.blit(self.img, [self.x,self.y])
        
    def chageimg(self, file):
        self.img = pygame.image.load("arduino/resources/images/"+file+".png")
    def addtext(self, text, font):
        self.text = font.render(text, True, [255,255,255]) 
class SerialEmulator(object):
    def __init__(self, device_port='./Serial/ttylcdi', client_port='./Serial/ttylcdo', baud=9600):
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
        if(self.inser == '@%clear'):
            lcd.clear()
            self.inser = self.old
            return(self.inser)
        elif("@%pos" in self.inser):
            x = self.inser[5]
            #print(x)
            y = self.inser[7:]
            #print(y)
            lcd.setpos(x, y)
            self.inser = self.old
            return(self.inser)
        else:
            return(self.inser)
    def available(self):
        return(self.serial.available())
    def begin(self, baud):
        print('sersetup')
        self.serial = SerialEmulator('./Serial/ttylcdi','./Serial/ttylcdo', baud)
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



Serial = SerialA() #setup serial
lcd = lcdclass()
Serial.begin(9600)

pygame.init()
lcd.begin("orange")
lcd.render()
lcd.clear()
print("started")
while 1:
    i = 0
    #print(Serial.available())
    if(Serial.available()):
        text = Serial.read(10)
        print(text)
        
        lcd.write(text)
        Serial.clear()
    lcd.render()
