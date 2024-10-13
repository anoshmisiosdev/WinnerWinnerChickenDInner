# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Riyan Anosh and Aditiya Kolekar                              #
# 	Created:      5/26/2024, 12:21:32 PM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain = Brain()

controller = Controller()
brain.screen.print("Hello V5")

motor1 = Motor(Ports.PORT1, False)  # Front left, direction reversed
motor2 = Motor(Ports.PORT2, True)  # Front right
motor3 = Motor(Ports.PORT3, False) # Back left, direction reversed
motor4 = Motor(Ports.PORT4, True) # Back right
motor5 = Motor(Ports.PORT5, False)
motor6 = Motor(Ports.PORT6, True)
holding = Pneumatics(Ports.PORT7)
motorgroupleft = MotorGroup(motor1, motor3)
motorgroupright = MotorGroup(motor2, motor4)
drivemode = DriveTrain(motorgroupleft, motorgroupright, 319.19, 295, 40, MM, 1)
escalator = Motor(Ports.PORT5, True)

slow_mode = controller.buttonL1
#bing bong

def autonomous():
    return

# monitor controller input
def check_controller():
    while True:
        # left motor group spin forward
        if controller.axis3.position() > 0:
            motorgroupleft.spin(FORWARD, controller.axis3.position, PERCENT)
        # left motor group spin backward
        elif controller.axis3.position() < 0:
            motorgroupleft.spin(REVERSE, abs(controller.axis3.position()), PERCENT)
        # no input then don't spin motor group
        else:
            motorgroupleft.spin(FORWARD, 0, PERCENT)

        # right motor group spin forward
        if controller.axis2.position() > 0:
            motorgroupright.spin(FORWARD, controller.axis2.position, PERCENT)
        # right motor group spin backward
        elif controller.axis2.position() < 0:
            motorgroupright.spin(REVERSE, abs(controller.axis2.position()), PERCENT)
        # no input then don't spin motor group
        else:
            motorgroupright.spin(FORWARD, 0, PERCENT)
        if controller.buttonA.pressing():
            openning = 0
            if openning == 1:
                holding.close()
                openning = 0
            else:
                holding.open()
                openning = 1
                
        




def drive():
    check_controller()


def user_control():
    while True:
        drive()

user_control()
