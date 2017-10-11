#Basic Claw Game
from gpiozero import Motor, Button, LED
from time import sleep
import pygame
pygame.mixer.pre_init(44100, -16, 2, 2048)
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
forwardButton = Button(7)
rightButton = Button(6)

#Init Claw Electromagnet
#clawMagnet = LED(18)

moveMusic = "musicFiles/movement.mp3"
clawMusic = "musicFiles/claw.mp3"

while True:
    print("Press enter to start game")
    pygame.mixer.music.load(moveMusic)
    input()
    print("Waiting for right button")
    rightButton.wait_for_press()
    pygame.mixer.music.play()
    leftRight.backward()
    sleep(0.5)
    while(rightButton.is_pressed) and (leftRightStop.is_pressed != 1):
        pass
    leftRight.stop()
    #pygame.mixer.music.pause()
    print("Waiting for forward button")
    forwardButton.wait_for_press()
    #pygame.mixer.music.unpause()
    forwardBack.forward()
    sleep(0.5)
    while(forwardButton.is_pressed) and (forwardBackStop.is_pressed != 1):
        pass
    forwardBack.stop()
    pygame.mixer.music.load(clawMusic)
    pygame.mixer.music.play(-1)
    #Claw Drop
    upDown.backward()
    downStop.wait_for_press()
    #Grab Candy
    upDown.stop()
    sleep(1)
    #Candy grabbed lift
    #pygame.mixer.music.load(moveMusic)
    #pygame.mixer.music.play(-1)
    pygame.mixer.music.rewind()
    upDown.forward()
    upStop.wait_for_press()
    upDown.stop()
    #Claw Up
    pygame.mixer.music.load(moveMusic)
    pygame.mixer.music.play()
    #Home left
    leftRight.forward()
    sleep(0.5)
    leftRightStop.wait_for_press()
    leftRight.stop()
    #Home right
    forwardBack.backward()
    sleep(0.5)
    forwardBackStop.wait_for_press()
    forwardBack.stop()
    pygame.mixer.music.stop()
        
    
