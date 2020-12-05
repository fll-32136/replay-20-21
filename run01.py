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
    straight(-200, 300)
    turn(-56,500)
    straight(-300, 1300)
    turn(45,400)
    straight(300,1250)
    turn(-45,400)
    straight(200,200)
    attachment(-500,900)
    ev3.speaker.beep()
    straight(-300,400)  
    # straight(-500,550)
    turn(-79,700)
    straight(450,1000)
    turn(90, 800)
    straight(200,1000)
    turn(90, -800)
    straight(200,500)
    attachment(300,-1400)
    attachment(-300, 950)
    # # straight_(250,1200)
    # # turn(-70,2800)
    # # straight(500,3000)

bench()