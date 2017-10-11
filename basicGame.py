#Basic Claw Game
from gpiozero import Motor, Button, LED
from time import sleep
import pygame
pygame.mixer.init()
#Init Motors
forwardBack = Motor(17,27)
leftRight = Motor(22,23)
upDown = Motor(9,25)

#Init Stop Switches
leftRightStop = Button(4)
forwardBackStop = Button(3)
upStop = Button(2)
downStop = Button(5)

#Init Buttons
forwardButton = Button(6)
rightButton = Button(7)

#Init Claw Electromagnet
#clawMagnet = LED(18)

moveMusic = "musicFiles/movement.mp3"
clawMusic = "musicFiles/movement.mp3"

while True:
    print("Press enter to start game")
    pygame.mixer.music.load(moveMusic)
    input()
    print("Waiting for forward button")
    forwardButton.wait_for_press()
    pygame.mixer.music.play()
    forwardBack.forward()
    while(forwardButton.is_pressed) and (forwardBackStop.is_pressed != 1):
        pass
    forwardBack.stop()
    pygame.mixer.music.pause()
    print("Waiting for right button")
    rightButton.wait_for_press()
    pygame.mixer.music.unpause()
    leftRight.forward()
    while(rightButton.is_pressed) and (leftRightStop.is_pressed != 1):
        pass
    leftRight.stop()
    pygame.mixer.music.load(clawMusic)
    pygame.mixer.music.play()
    #Claw Drop
    sleep(5) #Simulate claw drop
    #Claw Up
    pygame.mixer.music.load(moveMusic)
    pygame.mixer.music.play()
    #Home left
    leftRight.backward()
    sleep(0.5)
    leftRightStop.wait_for_press()
    leftRight.stop()
    #Home right
    forwardBack.forward()
    sleep(0.5)
    forwardBackStop.wait_for_press()
    forwardBack.stop()
    pygame.mixer.music.stop()
        
    
