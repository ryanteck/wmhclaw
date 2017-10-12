#Basic Claw Game
from gpiozero import Motor, Button, PWMLED
from time import sleep
import pygame
import random
pygame.mixer.pre_init(22050, -8, 2, 512)
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
clawMagnet = PWMLED(18,frequency=100)

moveMusic = "musicFiles/movement.ogg"
clawMusic = "musicFiles/clawLonger.ogg"

while True:
    print("Press enter to start game")
    
    print("Waiting for right button")
    rightButton.wait_for_press()
    pygame.mixer.music.load(moveMusic)
    pygame.mixer.music.play()
    leftRight.backward()
    sleep(0.3)
    while(rightButton.is_pressed) and (leftRightStop.is_pressed != 1):
        pass
    leftRight.stop()
    #pygame.mixer.music.pause()
    print("Waiting for forward button")
    forwardButton.wait_for_press()
    #pygame.mixer.music.unpause()
    forwardBack.forward()
    sleep(0.2)
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
    clawPwm = random.uniform(0.3,1)
    print(clawPwm)
    clawMagnet.value = clawPwm
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
    sleep(0.3)
    leftRightStop.wait_for_press()
    leftRight.stop()
    #Home right
    forwardBack.backward()
    sleep(0.3)
    forwardBackStop.wait_for_press()
    forwardBack.stop()
    pygame.mixer.music.stop()
    clawMagnet.value = 0 
        
    
