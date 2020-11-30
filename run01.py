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


def bench():
    #alignment: the right side of the back wall is at 1 line to the left of the second  vertical bolded line. there's also a tool
    straight(300,1350)
    straight(-200,100)
    turn(56,500)
    straight(-200, 300)
    turn(-56,500)
    straight(-300, 1300)
    turn(45,400)
    straight(300,1250)
    turn(-45,400)
    straight(200,200)
    attachment(-500,750)
    ev3.speaker.beep()
    # straight_(300,1500)  
    # straight(-500,550)
    turn(-70,500)
    # straight(450,1700)
    # turn(90, 750)
    # straight(200,700)
    # straight_(-300,1400)
    # # straight(-300, 950)
    # # straight_(250,1200)
    # # turn(-70,2800)
    # # straight(500,3000)

bench()