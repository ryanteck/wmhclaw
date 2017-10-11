from gpiozero import Motor, Button
from time import sleep

forwardBack = Motor(17,27)
leftRight = Motor(22,23)
upDown = Motor(9,25)

leftRightStop = Button(4)
forwardBackStop = Button(3)
upStop = Button(2)
downStop = Button(5)

print("initialization test")
input()

print("Homing")

leftRight.backward()
leftRightStop.wait_for_press()
leftRight.stop()

forwardBack.forward()
forwardBackStop.wait_for_press()
forwardBack.stop()

upDown.forward()
upStop.wait_for_press()

print("Homed")



