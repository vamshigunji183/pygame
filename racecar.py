# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import  pygame

pygame.init() #intiate the pygame
h=800
w=600
gameDisplay=pygame.display.set_mode((h,w)) #window

#naming window
pygame.display.set_caption('car race')

clock=pygame.time.Clock()
#check what is clock

crashed= False

while not crashed:
    #here we start our loop
    for event in pygame.event.get():
        #pygame event
        if event.type == pygame.QUIT:
            #this is handled by pygame
            crashed = True
            
        print(event)
        #this will print the event in the pygame
    pygame.display.update() #this will update the window or we can use flip
    #update vs flip
    
    #frames per second
    clock.tick(32)
pygame.quit()
quit()
    
    
        