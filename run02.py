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
import time
from line_square import *

right_motor = Motor(Port.A)
left_motor = Motor(Port.B) 
wheel_diameter = 56 
axle_track = 114
straight_robot = DriveBase(right_motor, left_motor, wheel_diameter, axle_track)
# right_att_motor = Motor(Port.D, positive_direction=Direction.CLOCKWISE, gears=None)
rightcolor = ColorSensor(Port.S1)
# leftcolor = ColorSensor(Port.S3)


#Alignment: Right DRIVE wheel at 3rd horizontal line, front of robot is at 7th to last vertical line(bold line)
#  remember to tilt a tad bit to the left
def run02():
    # launch to stepcounter
    straight(175, 3300)
    # time.sleep(1)
    # does stepcounter slowly
    straight(20, 10500)  
    # time.sleep(1)
    #backs up from stepcounter and turns
    straight(-200, 400)
    straight_robot.drive(-100, 0)
    colorstop(straight_robot, rightcolor, 9)
    straight(200, 295)
    # straight(-150, 800)
    pivot_turn(50, 1200)
    pivot_turn(50, 450)
    # # back up to the wall
    straight(-175, 1250)
    # # launch to pull up bar and drop health units
    left_att(2250, -200)
    # time.sleep(1)
    straight(100, 1550)
    # time.sleep(2)
    left_att(2300, 200)
    # launch to treadmill and does treadmill
    straight(-75, 1400)
    # remember this is the oldone pivot_turn(-50, 1580)
    turn(-85, 765) # 780 #740
    straight(170, 3560)
    right_att(8000, 2000)
    # after treadmill
    straight(-250, 300)
    pivot_turn(50, 1500)
    straight(-250, 1500)
    # aligns by backing up to the wall
    straight(250, 100)
    pivot_turn(50, 350)
    straight(250, 400)
    left_att(1200, -200)
    pivot_turn(-50, 1710)
    straight( 250, 200)
    left_att(1400, 200)
    straight(-100, 1150)
    pivot_turn(50, 460)
    # finishes row machine
    left_att(2000, -200)
    straight(-200, 800)
    turn(-85, 200)
    straight(-5000, 6000)
   
# run02()
    