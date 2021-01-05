#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()

left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
rline_sensor = ColorSensor(Port.S1)
lline_sensor = ColorSensor(Port.S3)

wheel_diameter = 46
axle_track = 114
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

BLACK = 6
WHITE = 85

DRIVE_SPEED = 50

r = rline_sensor.reflection()
l = lline_sensor.reflection()


strforever(100)
while True:
    if r <= BLACK:
        right_motor.Stop()

    elif l <= BLACK:
        left_motor.Stop()

    elif r <=  BLACK and l <= BLACK:
        robot.Stop()
        break

    else:
        continue

straight(500,75)

strforever(-100)
while True:
    if r <= BLACK:
        right_motor.Stop()

    elif l <= BLACK:
        left_motor.Stop()

    elif r <=  BLACK and l <= BLACK:
        robot.Stop()
        break

    else:
        continue