# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       luketierney                                                  #
# 	Created:      1/19/2023, 2:17:18 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *
import math
# Begin project code
timepertile = 1
timefor360 = 1
speed = 0
def go(ttime, one, two, three, four):
    global speed
    motor_1.set_velocity(speed*one, PERCENT)
    motor_2.set_velocity(speed*two, PERCENT)
    motor_3.set_velocity(speed*three, PERCENT)
    motor_4.set_velocity(speed*four, PERCENT)
    wait(ttime*1000, SECONDS)
    motor_1.stop()
    motor_2.stop()
    motor_3.stop()
    motor_4.stop()

def left(degree):
    global timefor360
    ttime = degree * (timefor360/360)
    go(ttime, 1, 1, 0, 0)
def right(degree):
    global timefor360
    ttime = degree * (timefor360/360)
    go(ttime, 0, 0, 1, 1)
def forward(tiles):
    global timepertile
    ttime = tiles * timepertile
    go(ttime, 1, 1, 1, 1)
def backward(tiles):
    global timepertile
    ttime = tiles * timepertile
    go(ttime, -1, -1, -1, -1)
def autoroller(degrees):
    motor_1.spin_for(FORWARD, degrees, DEGREES)
def joystickmovement():
    a1 = controller_1.axis1.position()
    a2 = controller_1.axis4.position()
    leftside = a1*a2/10000 
    rightside = a1*(-a2+100)/10000
    motor_1.set_velocity(speed*leftside, PERCENT)
    motor_2.set_velocity(-speed*leftside, PERCENT)
    motor_3.set_velocity(-speed*rightside, PERCENT)
    motor_4.set_velocity(speed*rightside, PERCENT)
def rollermovement():
    if controller_1.buttonR1.pressing():
        motor_5.set_velocity(100, PERCENT)
    elif controller_1.buttonR2.pressing():
        motor_5.set_velocity(-100, PERCENT)
    else:
        motor_5.set_velocity(0, PERCENT)
def when_started1():
    timeperfoot = 1 
    timefor360 = 2
    speed = 100
    timepertile = timeperfoot * 2
    motor_1.set_velocity(0, PERCENT)
    motor_2.set_velocity(0, PERCENT)
    motor_3.set_velocity(0, PERCENT)
    motor_4.set_velocity(0, PERCENT)


def onauton_autonomous_0():
    brain.timer.clear()
    backward(.25)
    autoroller(300)

def ondriver_drivercontrol_0():
    brain.timer.clear()
    brain.screen.set_pen_width(40)
    while True:
        controller_1.screen.set_cursor(1, 1)
        controller_1.screen.print(brain.timer.time(SECONDS), "Seconds                                               ")
        joystickmovement()
        rollermovement()
        if (brain.timer.time(SECONDS) >= 102) and (brain.timer.time(SECONDS) < 104):
            motor_6.set_velocity(100, PERCENT)
        if (brain.timer.time(SECONDS) >= 104):
            motor_6.set_velocity(0, PERCENT)
 

# create a function for handling the starting and stopping of all autonomous tasks
def vexcode_auton_function():
    # Start the autonomous control tasks
    auton_task_0 = Thread( onauton_autonomous_0 )
    # wait for the driver control period to end
    while( competition.is_autonomous() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the autonomous control tasks
    auton_task_0.stop()

def vexcode_driver_function():
    # Start the driver control tasks
    driver_control_task_0 = Thread( ondriver_drivercontrol_0 )

    # wait for the driver control period to end
    while( competition.is_driver_control() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the driver control tasks
    driver_control_task_0.stop()


# register the competition functions
competition = Competition( vexcode_driver_function, vexcode_auton_function )

when_started1()
