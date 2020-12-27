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

ev3=EV3Brick()


def bench():
    #alignment: the right side of the back wall is at 1 line to the left of the second  vertical bolded line. there's also a tool
    straight(300,1350)
    straight(-200,100)
    turn(56,500)
    straight(-100, 600)
    turn(-56,500)
    straight(-300, 1300)
    turn(45,400)
    straight(300,1350)
    turn(-45,200)
    straight(200,200)
    straight_(-500,700)
    
    straight(-300,400)
    # #cstraight(-500,550)
    turn(-79,700)
    straight(450,1000)
    turn(90, 800)
    straight(200,1300)
    # # # # straight_(250,1200)
    turn(400,1000)
    straight(-300,1250)
    #`turn(1400,200)
    # straight(100,100)
    # straight(300,-1000)
    # straight_(-500,-1000)
    # straight(-500,1300)
    # straight(500,1100)
    # straight(500,500)

# bench()
def run01_2():
    straight(200,1600)
    turn(-85,570)
    straight(200,600)
    turn(85,520)
    straight(-200,600)
    turn(-85,500)

    straight(200,2100)
    turn(85,587)
    straight(200,450)
    left_att(3000,-2000)
    straight(-200,450)
    turn(85,607)
    turn(85,1600)
    straight(-200,1000)

def run01_3 ():
    straight(200,1600)
    turn(-85,470)
    straight(200,600)
    turn(85,520)
    turn(-85,25)
    straight(-200,400)
    turn(-85,350)
    straight(200,200)
    turn(85,800)
    straight(200,500)
    left_att(2000,-500)
    left_att(1800,500)
    straight(-200,1650)
    turn(-85,550)

run01_3()
