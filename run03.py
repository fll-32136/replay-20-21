#!/usr/bin/env pybricks-micropython
# All imports
from pybricks.hubs import *
from math import *
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from common import *
from line_square import *
import time

# A basic drivebase

right_motor = Motor(Port.A)
left_motor = Motor(Port.B) 
wheel_diameter = 56 
axle_track = 114
straight_robot = DriveBase(right_motor, left_motor, wheel_diameter, axle_track)

# All objects

ev3 = EV3Brick()
gyro_sensor = GyroSensor(Port.S4)
leftcolorsensor=ColorSensor(Port.S3)
rightcolorsensor=ColorSensor(Port.S1)
BLACK=5
WHITE=55

# Alignment: Attachment position on the last line to the left

def run03():
    # Robot goes moves toward and completes dropping cubes in bench
    straight(400, 1550)
    turn(-90, 175)
    time.sleep(1)
    left_att(3000, -2000)
    # Goes back and moves turns toward boccia target
    straight(-1000, 1250)
    turn(-90, 230)
    straight(400, 1800)
    # Does a line square at the line next to basketball and continues toward boccia target
    line_square(8,5,70)
    straight(400, 400)
    turn(90, 950)
    # Backs up with a colorstop at the line right next to boccia target
    straight(-200, 1500)
    straight_robot.drive(-200, 0)
    colorstop(straight_robot, rightcolorsensor, 8)
    # Turns toward boccia target and drops all 8 cubes
    pivot_turn(-90, 600)
    straight(300, 550)
    right_att(650, -200)
    time.sleep(0.5)
    # Goes to robot dance and infinitely moves back and forth
    straight(-300, 500)
    turn(90, 500)
    straight(400, 1300)
    turn(90, 700)
    straight(-100, 1500)
    while True:
        straight(-100, 800)
        straight(100, 600)
# run03()