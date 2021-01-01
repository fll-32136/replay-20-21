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

def turn_forever(direction):
    motor = Motor(Port.A)
    motor1 = Motor(Port.B)
    wheel_diameter = 46
    axle_track = 114
    robot = DriveBase(motor, motor1, wheel_diameter, axle_track)
    robot.drive_time(0, direction, 0)

def left_att(Time, Speed):
    #Negative speed goes up (for lift att)
    robot = Motor(Port.C, positive_direction=Direction.CLOCKWISE, gears=None)
    robot.run_time(Speed, Time, then=Stop.HOLD, wait=True)

def right_att(Time, Speed): 
    robot = Motor(Port.D, positive_direction=Direction.CLOCKWISE, gears=None)
    robot.run_time(Speed, Time, then=Stop.HOLD, wait=True)

def strforever(Speed):
    motor = Motor(Port.A)
    motor1 = Motor(Port.B) 
    wheel_diameter = 56
    axle_track = 114
    robot = DriveBase(motor, motor1, wheel_diameter, axle_track)
    robot.drive(Speed, 0)

def strstop():
    motor = Motor(Port.A)
    motor1 = Motor(Port.B) 
    wheel_diameter = 56
    axle_track = 114
    robot = DriveBase(motor, motor1, wheel_diameter, axle_track)
    robot.stop()

def straight_(Speed, Time):
    motor = Motor(Port.C)
    motor1 = Motor(Port.D)
    wheel_diameter = 56
    axle_track = 114
    robot = DriveBase(motor, motor1, wheel_diameter, axle_track)
    robot.drive_time(Speed, 0, Time) #Time in seconds by thousands
    robot.stop(Stop.BRAKE)

# Use negative direction for right motor
def attachment(direction, degrees):
    motor = Motor(Port.C)
    motor1 = Motor(Port.D)
    wheel_diameter = 56
    axle_track = 114
    robot = DriveBase(motor, motor1, wheel_diameter, axle_track)
    robot.drive_time(math.pi * axle_track / 4, direction, degrees) #Time in seconds by thousands
    robot.stop(Stop.BRAKE)

# right_att(360, 1000)
# left_att(360, 1000)
# straight(1000, 1750)
# straight(25, 9000)

def color_finder():
    line_sensor = ColorSensor(Port.S3)
    print(line_sensor.reflection())

def color_stop(color_num):   
    line_sensor = ColorSensor(Port.S3)
    while line_sensor.reflection() != color_num:  #when color is not black
        straight(200,200) #go straight

def colorstop(straight_robot,colorsensor):
    while True:
        if colorsensor.reflection()<=5:
            straight_robot.stop()
            break
            

    # motor=Motor(Port.A)
    # motor1=Motor(Port.B)
    # colorsensor=ColorSensor(Port.S3)
    # robot = DriveBase(motor, motor1, wheel_diameter, axle_track)
    # BLACK=5
    # WHITE=54

