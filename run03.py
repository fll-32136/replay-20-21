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
gyro_sensor = GyroSensor(Port.S2)

# Alignment: Right wheel on 6th line with robot on back wall
# Attachment start position 2 cubes at the top

def gyro_finder():
    gyro_sensor = GyroSensor(Port.S2)
    print(gyro_sensor.angle())

left_motor = Motor(Port.B)
right_motor = Motor(Port.A)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

def gyro_stop(gyro_num):   
    gyro_sensor = GyroSensor(Port.S2)
    gyro_sensor.reset_angle(0)
    while gyro_sensor.angle() != gyro_num:
        if gyro_sensor.angle() > gyro_num:
            robot.drive(50,90)
        elif:
            robot.drive(50,-90)
        else:
    gyro_finder()

def run3():
    gyro_sensor.reset_angle(0)
    straight(200, 1810)
    gyro_stop(0)
    gyro_stop(-85)
    straight(-200, 60)
    attachment(-95, 580)
    straight(200, 200)
    wait(400)
    attachment(-95, 580)
    wait(400)
    straight(200, 250)
    wait(400)
    attachment(-95, 580)
    wait(400)
    straight(200, 250)
    wait(400)
    attachment(-95, 600)

run3()