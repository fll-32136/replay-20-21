#!/usr/bin/env pybricks-micropython
from pybricks.hubs import *
from math import *
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from common import *
from time import *
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
gyro_sensor = GyroSensor(Port.S4)

# Alignment: Right wheel on 6th line with robot on back wall
# Attachment start position 2 cubes at the top

# def gyro_finder():
#     gyro_sensor = GyroSensor(Port.S4)
#     print(gyro_sensor.angle())

# left_motor = Motor(Port.B)
# right_motor = Motor(Port.A)

# robot = DriveBase(left_motor, right_motor, wheel_diameter=46, axle_track=114)

# def gyro_stop(gyro_num):   
#     gyro_sensor = GyroSensor(Port.S4)
#     gyro_sensor.reset_angle(0)
#     while gyro_sensor.angle() != gyro_num:
#         if gyro_sensor.angle() < gyro_num:
#             robot.drive(50,20)
#         elif gyro_sensor.angle() > gyro_num:
#             robot.drive(50,-20)

def absolutly_not():
    straight(100, 3600)
    # robot.settings(0, 0, 100, 100)
    # robot.turn(-12.5)
    turn(-90, 185)
    # Negative speed makes attachment move 
    left_att(800, -1000)
    straight(-100, 1000)
    turn(-90, 420)
    straight(1000, 3600)
    turn(90, 700)
    straight(100, 600)
    turn(90, 300)
    straight(-100, 550)
    turn(-90, 200)
    straight(100, 200)
    right_att(650, -1000)
    turn(90, 500)
    straight(100,1500)
    turn(90, 750)
    straight(-100, 500)
    while True:
        straight(-100, 800)
        straight(100, 600)
absolutly_not()
    
# straight(200, 1810)
# gyro_stop(0)
# turn(90, 664)
# straight(200, 30)
# attachment(-95, 550)
# straight(200, 250)
# wait(400)
# attachment(-95, 600)
# wait(400)
# straight(200, 545)
# wait(400)
# attachment(-95, 590)
# wait(400)
# straight(200, 290)
# wait(400)
# attachment(-95, 610)