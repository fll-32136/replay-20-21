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
#Alignment: Right wheel at 3rd horizontal line, front of robot is at 2nd to last vertical line
# def stepcounter():
#     straight(175, 3000)
#     time.sleep(1)
#     straight(25, 8300)
#     #after stepcounter
#     straight(-175, 825)
#     pivot_turn(50, 1400)
#     pivot_turn(50, 500)
#     straight(-175, 1300)
#     straight(175, 2800)
#     #after pull-up bar
#     turn(50, 800)
#     straight(175, 1850)
#     while True:
#         straight(175, 250)
#         straight(-175, 225)
#     #after robot dance

# stepcounter()
#Alignment: Right wheel at 3rd horizontal line, front of robot is at front of big LEGO square
def run02():
    #Home to health units
    straight(250, 2400)
    time.sleep(1)
    straight_(-100,1500)
    time.sleep(1)
    straight(50, 1000)
    straight_(300,500)
    straight(-150,700)
    # pivot_turn(50, 1400)
    # straight(250, 500)

run02()
    