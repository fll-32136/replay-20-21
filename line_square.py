#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from common import *

ev3 = EV3Brick()

left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
rline_sensor = ColorSensor(Port.S1)
lline_sensor = ColorSensor(Port.S3)

wheel_diameter = 46
axle_track = 114
straight_robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

leftdrive = Motor(Port.B, positive_direction=Direction.CLOCKWISE, gears=None)
rightdrive= Motor(Port.A, positive_direction=Direction.CLOCKWISE, gears=None)




def line_square(RBLACK,LBLACK):
    r = rline_sensor.reflection()
    l = lline_sensor.reflection()
    print("right = ",r, "left =",l)

    straight_robot.drive(100,0)
    while True:
        r = rline_sensor.reflection()
        l = lline_sensor.reflection()
        if r <= RBLACK:
            straight_robot.stop()
            wait(100)
            while l > LBLACK:
                r = rline_sensor.reflection()
                l = lline_sensor.reflection()
                print("right = ",r, "left =",l)
                leftdrive.run(-50)
            leftdrive.stop()
            while r > RBLACK:
                r = rline_sensor.reflection()
                l = lline_sensor.reflection()
                print("right = ",r, "left =",l)
                rightdrive.run(50)
            rightdrive.stop()
            break

        if l <= LBLACK:
            straight_robot.stop()
            wait(100)
            while r > RBLACK:
                r = rline_sensor.reflection()
                l = lline_sensor.reflection()
                print("right = ",r, "left =",l)
                rightdrive.run(50)
            rightdrive.stop()
            while l > LBLACK:
                r = rline_sensor.reflection()
                l = lline_sensor.reflection()
                print("right = ",r, "left =",l)
                leftdrive.run(-50)
            leftdrive.stop()
            break

        if r <= RBLACK and l <= LBLACK:
            break

# r = rline_sensor.reflection()
# l = lline_sensor.reflection()
# print("right = ",r, "left =",l)