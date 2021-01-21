#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from common import *

ev3 = EV3Brick()

left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
rline_sensor = ColorSensor(Port.S1)
lline_sensor = ColorSensor(Port.S3)

wheel_diameter = 46
axle_track = 114
straight_robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

leftdrive = Motor(Port.B, positive_direction=Direction.CLOCKWISE, gears=None)
rightdrive= Motor(Port.A, positive_direction=Direction.CLOCKWISE, gears=None)




def line_square(RBLACK,LBLACK,SPEED): #Takes in the needed color values and speed
    
    r = rline_sensor.reflection() #Redefines the color sensors to r and l
    l = lline_sensor.reflection()

    straight_robot.drive(SPEED,0) #Makes robot go straight forever
    while True:
        r = rline_sensor.reflection() #Restates the color sensor values
        l = lline_sensor.reflection()

        if r <= RBLACK: #If right color sensor hits black, it will stop
            straight_robot.stop()
            wait(100)
            while l > LBLACK: #The left wheel moves unit it is on black
                r = rline_sensor.reflection() #Restates the color sensor values
                l = lline_sensor.reflection()
                leftdrive.run(50)
            leftdrive.stop()
            while r > RBLACK: #To be sure it's completely on the line, right wheel moves back until it is on black
                r = rline_sensor.reflection() #Restates the color sensor values
                l = lline_sensor.reflection()
                rightdrive.run(-50)
            rightdrive.stop()
            break

        if l <= LBLACK: #If right color sensor hits black, it will stop
            straight_robot.stop()
            wait(100)
            while r > RBLACK: #The right wheel moves unit it is on black
                r = rline_sensor.reflection() #Restates the color sensor values
                l = lline_sensor.reflection()
                rightdrive.run(50)
            rightdrive.stop()
            while l > LBLACK: #To be sure it's completely on the line, left wheel moves back until it is on black
                r = rline_sensor.reflection() #Restates the color sensor values
                l = lline_sensor.reflection()
                leftdrive.run(-50)
            leftdrive.stop()
            break

        if r <= RBLACK and l <= LBLACK: #If both sensors sense black at the same time, it just stops
            break