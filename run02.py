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
#Alignment: Right DRIVE wheel at 3rd horizontal line, front of robot is at 7th to last vertical line(bold line)
#  remember to tilt a tad bit to the left
def run02():
    # launch to stepcounter
    straight(175, 3500)
    time.sleep(1)
    # does stepcounter slowly
    straight(25, 7850)
    time.sleep(1)
    # backs up from stepcounter and turns
    straight(-150, 1150)
    pivot_turn(50, 1400)
    pivot_turn(50, 450)
    # back up to the wall
    straight(-175, 1300)
    # launch to pull up bar and drop health units
    left_att(2200, -200)
    time.sleep(1)
    straight(100, 1500)
    time.sleep(2)
    left_att(2200, 200)
    straight(-75, 1650)
    pivot_turn(-50, 1550)
    straight(175, 3350)
    right_att(2000,2000)
    right_att(2000,2000)
    straight(-175, 9000)

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
    