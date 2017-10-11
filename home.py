from gpiozero import Motor, Button
from time import sleep

forwardBack = Motor(17,27)
leftRight = Motor(22,23)
upDown = Motor(9,25)

upDown.backward()
sleep(5)
upDown.stop()

leftRightStop = Button(4)
forwardBackStop = Button(3)
upStop = Button(2)
downStop = Button(5)

print("initialization test")
input()

print("Homing")

leftRight.forward()
leftRightStop.wait_for_press()
leftRight.stop()

forwardBack.backward()
forwardBackStop.wait_for_press()
forwardBack.stop()

upDown.forward()
upStop.wait_for_press()
upDown.stop()

print("Homed")



