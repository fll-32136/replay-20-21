#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

ev3 = EV3Brick()

ev3=EV3Brick()
#initializing  color sensor and motors
leftcolorsensor=ColorSensor(Port.S3)
rightcolorsensor=ColorSensor(Port.S1)
BLACK=5
WHITE=55
# intializing drivebase and related values
right_motor = Motor(Port.A)
left_motor = Motor(Port.B) 
wheel_diameter = 56 
axle_track = 114
drivebase = DriveBase(right_motor, left_motor, wheel_diameter, axle_track)
right_att_motor = Motor(Port.D, positive_direction=Direction.CLOCKWISE, gears=None)

left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
left_line_sensor = ColorSensor(Port.S3)
right_line_sensor = ColorSensor(Port.S1)

wheel_diameter = 56
axle_track = 114
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

WHITE = 85

strforever(100)
while left_line_sensor != WHITE:
    pivot_forever(-85,0)
