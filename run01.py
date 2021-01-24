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
from line_square import *

import time


ev3=EV3Brick()
#initializing  color sensors
leftcolorsensor=ColorSensor(Port.S3)
rightcolorsensor=ColorSensor(Port.S1)
BLACK=5
WHITE=55




def run01_6():
    # knocks backrest off
    straight(200,1700)
    turn(-85,400)    
    straight(200,600)
    # flattens bench
    turn(85,520)
    straight(-200,450)
    turn(-85,450)
    # turns and goes staight before squaring up to boccia line
    straight(200,200)
    turn(85,400)
    straight(-200,300)
    turn(85,970)
    straight(-250,1075)
    turn(-50,1350)
    straight(200,850)
    line_square(11,5,110)
    # Turns to Boccia
    turn(-50,390)
    straight(200,900)
    straight(-100,1400)
    # Turn for basketball
    turn(75,815)
    straight(111,1570)
    # Cube goes in basketball
    straight(-200,450)
    turn(-85,500)
    straight(-200, 500)
    # turns back to bring health unit into base
    pivot_turn(-85,1350)
    straight_robot.drive(-200,20)
    # robot comes back to base into base
    wait(4400)
    straight_robot.stop()
# run01_6()

def run01_7():
    # knocks backrest off
    straight(200,1700)
    turn(-85,400)    
    straight(200,600)
    # flattens bench
    turn(85,520)
    straight(-200,450)
    turn(-85,450)
    # turns and goes staight before squaring up to boccia line
    straight(200,200)
    turn(85,400)
    straight(-200,300)
    turn(85,870)
    line_square(11,5,100)
    straight(-250,1375)
    turn(-50,1350)
    straight(200,850)
    line_square(11,5,110)
    # Turns to Boccia
    turn(-50,350)
    straight(200,900)
    straight(-100,1360)
    # Turn for basketball
    turn(75,707)
    straight(111,1540)
    # # Cube goes in basketball
    straight(-200,575)
    turn(-85,1300)
    # # turns back to bring health unit into base
    straight_robot.drive(-200,20)
    # # robot comes back to base into base
    wait(4400)
    straight_robot.stop()
# run01_7()