#!/usr/bin/env pybricks-micropython
from pybricks.hubs import *
from math import *
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import math
def straight(Speed, Time):
    motor = Motor(Port.A)
    motor1 = Motor(Port.B)
    wheel_diameter = 46
    axle_track = 114
    robot = DriveBase(motor, motor1, wheel_diameter, axle_track)
    robot.drive_time(Speed, 0, Time) #Time in seconds by thousands
    robot.stop(Stop.BRAKE)

# # def straight_d(Speed, Distance/Speed):
#     straight(Speed, Time)


def pivot_turn(direction, degrees):
    left_motor = Motor(Port.A)
    right_motor = Motor(Port.B)
    wheel_diameter = 56
    axle_track = 114
    robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
    robot.drive_time(math.pi * axle_track / 4, direction, degrees)
    robot.stop(Stop.BRAKE)

def turn(direction, degrees):
    motor = Motor(Port.A)
    motor1 = Motor(Port.B)
    wheel_diameter = 46
    axle_track = 114
    robot = DriveBase(motor, motor1, wheel_diameter, axle_track)
    robot.drive_time(0, direction, degrees)
    robot.stop(Stop.BRAKE)

def left_att(degrees, Speed):
    left_att_motor = Motor(Port.C)
    wheel_diameter = 46
    axle_track = 114
    left_att_move = DriveBase(left_att_motor, wheel_diameter, axle_track)
    left_att_move.drive_time(degrees, 0, Speed)
    left_att_move.stop(Stop.BRAKE)

def right_att(degrees, Speed):
    right_att_motor = Motor(Port.D)
    wheel_diameter = 46
    axle_track = 114
    right_att_move = DriveBase(right_att_motor, wheel_diameter, axle_track)
    right_att_move.drive_time(degrees, 0, Speed)
    right_att_move.stop(Stop.BRAKE)

def straight_(Speed, Time):
    motor = Motor(Port.C)
    motor1 = Motor(Port.D)
    wheel_diameter = 56
    axle_track = 114
    robot = DriveBase(motor, motor1, wheel_diameter, axle_track)
    robot.drive_time(Speed, 0, Time) #Time in seconds by thousands
    robot.stop(Stop.BRAKE)

# right_att(360, 1000)
# left_att(360, 1000)
# straight(1000, 1750)
# straight(25, 9000)