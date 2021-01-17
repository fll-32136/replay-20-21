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
#initializing  color sensor and motors
leftcolorsensor=ColorSensor(Port.S3)
rightcolorsensor=ColorSensor(Port.S1)
BLACK=5
WHITE=55
# intializing drivebase and related values
# right_motor = Motor(Port.A)
# left_motor = Motor(Port.B) 
# wheel_diameter = 46 
# axle_track = 114
# drivebase = DriveBase(right_motor, left_motor, wheel_diameter, axle_track)
# right_att_motor = Motor(Port.D, positive_direction=Direction.CLOCKWISE, gears=None)

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

def run01_3():
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
    straight(-200,2200)
    turn(-85,650)
    straight(-199,701)
    straight(100,4000)
    straight(-200,650)
    turn(-200,190)
    straight(-1000,3000)

def run01_4():
    straight(150,2000)
    turn(-85,470)
    straight(150,800)
    turn(85,520)
    turn(-85,25)
    straight(-150,500)
    turn(-85,350)
    straight(150,150)
    turn(85,800)
    straight(150,625)
    left_att(2000,-500)
    left_att(1800,500)
    straight(-150,2750)
    turn(-85,650)
    straight(-150,875)
    straight(100,4000)
    straight(-150,812.5)
    turn(-200,190)
    straight(-750,2250)

def run01_5():
    straight(200,1700)
    turn(-85,400)
    straight(300,400)
    #knocks off bench
    turn(85,520)
    straight(-200,450)
    turn(-85,450)
    straight(200,200)
    turn(85,900)
    straight(200,500)
    left_att(2000,-700)
    left_att(1800,500)
    straight(-250,800)
    turn(-100,1500)
    strforever(100)
    colorstop(rightcolorsensor) 
    #drops attachment
    # wait(100)

def run01_6():
    straight(200,1700)
    turn(-85,400)    
    straight(200,600)
    turn(85,520)
    straight(-200,450)
    turn(-85,450)
    straight(200,200)
    turn(85,400)
    straight(-200,300)
    turn(85,740)
    # line_square(11,7,70)
    # left_att(2000,-700)
    # left_att(1800,500)
    # wait(100)
    straight(-250,1000)
    turn(-50,1250)
    # print("squaring to line")
    straight(200,750)
    line_square(11,5,110)
    turn(-50,302)
    straight(200,900)
    straight(-200,750)
    turn(75,775)
    straight(111,1500)
    straight(-200,850)
    turn(-85,1400)
    straight_robot.drive(-200,20)
    wait(3500)
    straight_robot.stop()
# run01_6()
# straight(-150,2500)