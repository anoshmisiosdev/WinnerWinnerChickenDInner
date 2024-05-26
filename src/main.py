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
escalator = Motor(Ports.PORT5, True)
#bing bong
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
    
def user_control():
    while True:
        drive()
