#import impotant stuff
import datetime
import os, pygame
from pygame.locals import *
from time import sleep
from multiprocessing import Process
#import custom libarys
from script import script, setup, init
from classes import *
starttime = datetime.datetime.now()
#Renderer
def render():
    screen.fill(0)
    background.rendernz()

    pin.render()
    pygame.display.set_caption("Arduino")
    pygame.display.flip()
    #event handle
    #print(Serial.outlen)
    if(Serial.outlen >= 240):
        #print("clearing")
        Serial.clear()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit() 
            exit(0) 
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            i = 0
            #pin clicker
            while i != 14:
                if(pos[0] >= vars(pin)['pin'+str(i)].x and pos[0] <= vars(pin)['pin'+str(i)].xm and pos[1] >= vars(pin)['pin'+str(i)].y and pos[1] <= vars(pin)['pin'+str(i)].ym):
                    if(vars(pin)['pin'+str(i)].st == 1):
                        pin.changeto(i, 0)
                    elif(vars(pin)['pin'+str(i)].st == 0):
                        pin.changeto(i, 1)
                i= i + 1
            i = 0
            while i != 6:
                if(pos[0] >= vars(pin)['pinA'+str(i)].x and pos[0] <= vars(pin)['pinA'+str(i)].xm and pos[1] >= vars(pin)['pinA'+str(i)].y and pos[1] <= vars(pin)['pinA'+str(i)].ym):
                    if(vars(pin)['pinA'+str(i)].st == 1):
                        pin.changeto(i+14, 0)
                    elif(vars(pin)['pinA'+str(i)].st == 0):
                        pin.changeto(i+14, 1)
                i= i + 1



#config

#Do not touch
screenY = 480
screenX = 640
i= 0

# 2 - Initialize the display
pygame.init()
screen=pygame.display.set_mode((screenX, screenY))
#setup
Serial = SerialA() #setup serial
initcl(render, screen) #initiliies classes
background = Box(0, 0, 'background') #make the background
pin = pin()#load pins 
lcd = lcdC()
render()#render everything
init(render, pin, Serial, lcd, starttime)#initilise script and functions

#arduino section
setup()#run setup function
while True:
    script()#run script function
    render()#render screen