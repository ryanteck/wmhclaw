from gpiozero import Motor, Button
from time import sleep

forwardBack = Motor(17,27)
leftRight = Motor(22,23)
upDown = Motor(20,21)

fowardButton = Button(2)
leftButton = Button(3)

#leftRightStop = Button()
#forwardBackStop = Button()
#upStop = Button()
#downStop = Button()

print("initialization test")
read_line()

print("Homing")

leftRight.backward()
forwardBack.forward()
read_line()
leftRight.stop()
forwardBack.stop()
print("Homed")
read_line()
print("Moving to the right")
leftRight.forward()
#Stop
leftRight.stop()
print("Moving to the left")
leftRight.backward()
#Stop
leftRight.stop()


