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
    straight(175, 3500)
    time.sleep(1)
    straight(25, 8160)
    #after stepcounter
    straight(-225, 800)
    pivot_turn(50, 1400)
    pivot_turn(50, 450)
    straight(-175, 1300)
    left_att(2000, -200)
    straight(175, 880)
    left_att(2000, 200)
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
    