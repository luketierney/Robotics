#region VEXcode Generated Robot Configuration
# Imports
from vex import *
import urandom
import math

# Brain should be defined by default
brain=Brain()

# Robot configuration code
motor_1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
motor_2 = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
motor_3 = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
motor_4 = Motor(Ports.PORT4, GearSetting.RATIO_18_1, False)
motor_5 = Motor(Ports.PORT5, GearSetting.RATIO_18_1, False)
motor_6 = Motor(Ports.PORT6, GearSetting.RATIO_18_1, False)
controller_1 = Controller(PRIMARY)

# wait for rotation sensor to fully initialize
wait(30, MSEC)
#endregion VEXcode Generated Robot Configuration
# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       luketierney                                                  #
# 	Created:      1/19/2023, 2:17:18 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Begin project code
timeperfoot = 1
timefor360 = 1
speed = 100
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
    Left = controller_1.axis2.position()
    Right = controller_1.axis3.position()
    motor_1.set_velocity(speed*Left/100, PERCENT)
    motor_2.set_velocity(-speed*Left/100, PERCENT)
    motor_3.set_velocity(-speed*Right/100, PERCENT)
    motor_4.set_velocity(speed*Right/100, PERCENT)
def rollermovement():
    if controller_1.buttonR1.pressing():
        motor_5.set_velocity(100, PERCENT)
    elif controller_1.buttonR2.pressing():
        motor_5.set_velocity(-100, PERCENT)
    else:
        motor_5.set_velocity(0, PERCENT)
def endgame():
    if controller_1.buttonL1.pressing() and (brain.timer.time(SECONDS) >= 95):
        motor_1.spin_for(FORWARD, 5, TURNS, wait=False)
def when_started1():
    global timepertile, timeperfoot
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
        endgame()
        wait(100)
 

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
