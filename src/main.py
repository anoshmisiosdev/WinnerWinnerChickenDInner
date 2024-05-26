# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Riyan Anosh                                                  #
# 	Created:      5/26/2024, 12:21:32 PM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

    # Brain should be defined by default
brain=Brain()
controller=Controller()
brain.screen.print("Hello V5")
motor1 = Motor(Ports.PORT1, False)  # Front left, direction reversed
motor2 = Motor(Ports.PORT2, True)  # Front right
motor3 = Motor(Ports.PORT3, False) # Back left, direction reversed
motor4 = Motor(Ports.PORT4, True) # Back right
motor5 = Motor(Ports.PORT5, False)
motor6 = Motor(Ports.PORT6, True)
motorgroupleft = MotorGroup(motor1, motor3, motor5)
motorgroupright = MotorGroup(motor2, motor4, motor6)
drivemode = DriveTrain(motorgroupleft, motorgroupright, 319.19, 295, 40, MM, 1)
escalator = Motor(Ports.PORT5, True)
#bing bong
def autonomous():
    return
def drive():
    if (abs(controller.axis1.position()))>5:
        forward=-controller.axis1.position()
    else:
        forward=0
    if(abs(controller.axis3.position())>5):
        turn=controller.axis3.position()
    else:
        turn=0
    if(abs(turn)+abs(forward))>100:
        max=(abs(turn)+abs(forward))/100
    else:
        max=1
    rightpower=(forward+turn)/max
    leftpower=(forward-turn)/max
    motorgroupleft.spin(leftpower)
    motorgroupright.spin(rightpower)
def user_control():
    while True:
        drive()


comp = Competition(user_control, autonomous)
pre_autonomous()
user_control()