# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       prasu                                                        #
# 	Created:      10/12/2024, 8:43:44 PM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

brain.screen.print("Hello V5")
# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Riyan Anosh and Aditiya Kolekar                              #
# 	Created:      5/26/2024, 12:21:32 PM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
controller = Controller()
motor1 = Motor(Ports.PORT1, False)  # Front left, direction reversed
motor2 = Motor(Ports.PORT2, True)  # Front right
motor3 = Motor(Ports.PORT3, False) # Back left, direction reversed
motor4 = Motor(Ports.PORT4, True) # Back right
motor6 = Motor(Ports.PORT6, True)
holding = Pneumatics(Ports.PORT7)
motorgroupleft = MotorGroup(motor1, motor3)
motorgroupright = MotorGroup(motor2, motor4)
drivemode = DriveTrain(motorgroupleft, motorgroupright, 319.19, 295, 40, MM, 1)
escalator = Motor(Ports.PORT5, True)

# create competition object
competition = Competition(driver, autonomous)

# create vision object
vision_1 = Vision(Ports.PORT1, 100, dark_blue)
brightness = 0

#bing bong  

# monitor Controller input
def check_Controller():
    while True:
        # left motor group spin forward
        if controller.axis3.position() > 0:
            motorgroupleft.spin(FORWARD, controller.axis3.position(), PERCENT)
        # left motor group spin backward
        elif controller.axis3.position() < 0:
            motorgroupleft.spin(REVERSE, abs(controller.axis3.position()), PERCENT)
        # no input then don't spin motor group
        else:
            motorgroupleft.spin(FORWARD, 0, PERCENT)

        # right motor group spin forward
        if controller.axis2.position() > 0:
            motorgroupright.spin(FORWARD, controller.axis2.position(), PERCENT)
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
      
       
def pre_auton():
    biggest = vision_1.largest_object.width
    
    # determines best brightness level based on how well the object can be seen
    for i in range(0, 20):
        brightness += 5
        current = vision_1.largest_object.width
        if current > biggest:
            biggest = current
            current = 0
        
    
                   
def driver():
    brain.screen.print("Driver mode")
    
def autonomous():
    brain.screen.print("Auton mode")
    
    
check_Controller()
                
        










        
