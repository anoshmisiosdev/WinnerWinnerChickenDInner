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
motorgroupleft = MotorGroup(motor1, motor3)
motorgroupright = MotorGroup(motor2, motor4)
drivemode = DriveTrain(motorgroupleft, motorgroupright, 319.19, 295, 40, MM, 1)
escalator = Motor(Ports.PORT5, True)
#bing bong
def autonomous():
    return
def drive():
    motorgroupleft.spin(FORWARD, controller.axis3.value)
    motorgroupright.spin(FORWARD, controller.axis2.value)
def user_control():
    while True:
        drive()

user_control()