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

# Begin project code
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
def aclaw(movement, ttime):
    motor_A6.set_velocity(movement, PERCENT)
    motor_A6.stop()
def joystickmovement():
    a1 = controller_3.axis1.position()
    a2 = controller_4.axis1.position()
    a2 += 100
    leftside = a1*a2/10000 
    rightside = a1*(-a2+100)/10000
    go(.0005, leftside, leftside, rightside, rightside)
def armvert():
    if controller_L1.buttonUp.pressing():
        motor_A5.set_velocity(25, PERCENT)
    else:
        motor_A5.stop()
def claw():
    if controller_R1.buttonUp.pressing():
        motor_A6.set_velocity(25, PERCENT)
    elif controller_R2.buttonUp.pressing():
        motor_A6.set_velocity(-25, PERCENT)
    else:
        motor_A6.stop()
def when_started1():
    timeperfoot = 1 
    timefor360 = 2
    speed = 100
    timepertile = timeperfoot * 2
    motor_1.set_velocity(0, PERCENT)

def onauton_autonomous_0():
    brain.timer.clear()
    for each in range(0,1):
        pass

def ondriver_drivercontrol_0():
    brain.timer.clear()
    while True:
        joystickmovement()
        armvert()
        claw()
        if brain.timer.time(SECONDS) >= 104:
            break

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
