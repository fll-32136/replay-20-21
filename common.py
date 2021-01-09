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

straight_wheel_diameter = 56
turn_wheel_diameter = 46
axle_track = 114
motor_a = Motor(Port.A)
motor_b = Motor(Port.B)
motor_c = Motor(Port.C)
motor_d = Motor(Port.D)
robot = DriveBase(motor_a, motor_b, straight_wheel_diameter, axle_track)
robot_turn = DriveBase(motor_a, motor_b, turn_wheel_diameter, axle_track)
robot_att = DriveBase(motor_c, motor_d, wheel_diameter, axle_track)

def straight(Speed, Time):
    robot.drive_time(Speed, 0, Time) #Time in seconds by thousands
    robot.stop(Stop.BRAKE)

def gyrorun(Speed, Time):
    gy = GyroSensor(Port.S2) 
    gy.reset_angle(0)
    while True:
        print(gy.angle())
        straight(100,1000)
        if gy.angle() >= 7:
            y = gy.angle()*6.25
            turn(-500, y)
        if gy.angle() <= (-7) :
            y = -(gy.angle())*6.25
            turn(500, y) 

def pivot_turn(direction, degrees):
    robot_turn.drive_time(math.pi * axle_track / 4, direction, degrees)
    robot_turn.stop(Stop.BRAKE)

def turn(direction, degrees):
    robot_turn.drive_time(0, direction, degrees)
    robot_turn.stop(Stop.BRAKE)

def turn_forever(direction):
    while True:
        pivot_turn(50,100)

def turn_forever(direction):
    robot_turn.drive_time(0, direction, 0)

def left_att(Time, Speed):
    #Negative speed goes up (for lift att)
    left_att_motor = Motor(Port.C, positive_direction=Direction.CLOCKWISE, gears=None)
    left_att_motor.run_time(Speed, Time, then=Stop.HOLD, wait=True)

def right_att(Time, Speed): 
    right_att_motor = Motor(Port.D, positive_direction=Direction.CLOCKWISE, gears=None)
    right_att_motor.run_time(Speed, Time, then=Stop.HOLD, wait=True)

def strforever(Speed):
    robot.drive(Speed, 0)

def strstop():
    robot.stop()

def straight_att(Speed, Time):
    robot_att.drive_time(Speed, 0, Time) #Time in seconds by thousands
    robot_att.stop(Stop.BRAKE)

# Use negative direction for right motor
def attachment(direction, degrees):
    robot.drive_time(math.pi * axle_track / 4, direction, degrees) #Time in seconds by thousands
    robot.stop(Stop.BRAKE)

# right_att(360, 1000)
# left_att(360, 1000)
# straight(1000, 1750)
# straight(25, 9000)

def color_finder():
    line_sensor = ColorSensor(Port.S3)
    print(line_sensor.reflection())



def colorstop(colorsensor):
    while True:
        if colorsensor.reflection()<=9:
            robot.stop()
            break
    robot.stop()

def infiniteturn():
    while True:
        pivot_turn(300,1000)



    # motor=Motor(Port.A)
    # motor1=Motor(Port.B)
    # colorsensor=ColorSensor(Port.S3)
    # robot = DriveBase(motor, motor1, wheel_diameter, axle_track)
    # BLACK=5
    # WHITE=54
