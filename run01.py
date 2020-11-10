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
    straight(500,1350)
    wait(100)
    straight(-500,100)
    turn(35,300)
    straight(-500,200)
    wait(100)
    straight(500,250)
    turn(-35,400)
    straight(80,55)
    straight_(-3000,1500) 
    straight(-500,150)
    straight_(150,1500) 
    straight(-150,550) 
    turn(-70,550)
    straight(500,1550)
    turn(70,650)
    straight(500,645)
    straight_(-250,1500)
    straight(-500, 1250)
    straight_(250,1200)
    # straight(80,150)
    turn(-70,2700)
    straight(500,3000)

bench()