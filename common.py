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
    while True:
        pivot_turn(50,100)

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

def colorstop(straight_robot,colorsensor,colorvalue): #Takes in which color sensor you are using and the value of the color
    while True:
        if colorsensor.reflection()<=colorvalue: #if the color sensor you chose has the same value as what you put in,
            straight_robot.stop() #the robot stops
            break
    straight_robot.stop()