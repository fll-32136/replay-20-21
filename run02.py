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
#Alignment: Right wheel at 2nd horizontal line, front of robot is at 2nd to last vertical line
def stepcounter():
    straight(175, 3000)
    time.sleep(1)
    straight(25, 8300)
    straight(-175, 825)
    pivot_turn(50, 1400)
    pivot_turn(50, 500)
    straight(-175, 1300)
    straight(175, 2800)
    turn(50, 800)
    straight(175, 1850)
    while True:
        straight(175, 250)
        straight(-175, 250)