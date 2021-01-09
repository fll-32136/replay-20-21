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

# right_motor = Motor(Port.A)
# left_motor = Motor(Port.B) 
# wheel_diameter = 56 
# axle_track = 114
# straight_robot = DriveBase(right_motor, left_motor, wheel_diameter, axle_track)
# right_att_motor = Motor(Port.D, positive_direction=Direction.CLOCKWISE, gears=None)

#Alignment: Right DRIVE wheel at 3rd horizontal line, front of robot is at 7th to last vertical line(bold line)
#  remember to tilt a tad bit to the left
def run02():
    # launch to stepcounter
    straight(175, 3300)
    time.sleep(1)
    # does stepcounter slowly
    straight(25, 7725)  #used to be 7850
    time.sleep(1)
    # backs up from stepcounter and turns
    straight(-150, 925)
    pivot_turn(50, 1400)
    pivot_turn(50, 450)
    # back up to the wall
    straight(-175, 1250)
    # launch to pull up bar and drop health units
    left_att(2200, -200)
    time.sleep(1)
    straight(100, 1550)
    
    time.sleep(2)
    left_att(2300, 200)

    # launch to treadmill and does treadmill
    straight(-75, 1725)

    # remember this is the oldone pivot_turn(-50, 1580)
    pivot_turn(-50, 1580)
    straight(170, 3500)
    right_att(8000, 2000)
    right_att(4000, 2000)

'''
    straight_robot.drive(250, 0)
    time.sleep(1.5)
    right_att_motor.run(-1000)
    time.sleep(3)
    straight_robot.stop()
    right_att_motor.stop()
    # right_att(2000,2000)
    # right_att(2000,2000)
    '''
    # after treadmill, aligns by backing up to the wall
    # straight(-175, 900)
    # pivot_turn(50, 1600)
    # straight(-250, 1500)
    # # launches to row machine
    # straight(250, 100)
    # pivot_turn(50, 350)
    # straight(250, 400)
    # pivot_turn(-50, 1900)
    # pivot_turn(-50, 150)
    # # does row machine
    # left_att(300, -200)
    # straight(100, 500)
    # left_att(600, 200)
    # straight(-100, 1400)
    # pivot_turn(50, 550)
#buuin
'''
    #do the lifty thing later
    straight(-175, 650)
    turn(-50, 1350)

    #after pull-up bar
    turn(50, 800)
    straight(175, 1850)
    while True:
        straight(175, 250)
        straight(-175, 225)
    #after robot dance
'''
run02()
    