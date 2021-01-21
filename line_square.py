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



# Takes in the needed color values and speed
def line_square(RBLACK,LBLACK,SPEED): 
    
    # Redefines the color sensors to r and l
    r = rline_sensor.reflection() 
    l = lline_sensor.reflection()

    # Makes robot go straight forever
    straight_robot.drive(SPEED,0) 
    while True:
        # Restates the color sensor values
        r = rline_sensor.reflection() 
        l = lline_sensor.reflection()

        # If right color sensor hits black, it will stop
        if r <= RBLACK: 
            straight_robot.stop()
            wait(100)
            # The left wheel moves unit it is on black
            while l > LBLACK: 
                # Restates the color sensor values
                r = rline_sensor.reflection() 
                l = lline_sensor.reflection()
                leftdrive.run(50)
            leftdrive.stop()
            # To be sure it's completely on the line, 
            # the right wheel moves back until it is on black
            while r > RBLACK: 
                #  Restates the color sensor values
                r = rline_sensor.reflection() 
                l = lline_sensor.reflection()
                rightdrive.run(-50)
            rightdrive.stop()
            break

        # If right color sensor hits black, it will stop
        if l <= LBLACK: 
            straight_robot.stop()
            wait(100)
            # The right wheel moves unit it is on black
            while r > RBLACK: 
                # Restates the color sensor values
                r = rline_sensor.reflection() 
                l = lline_sensor.reflection()
                rightdrive.run(50)
            rightdrive.stop()
            # To be sure it's completely on the line, 
            # the left wheel moves back until it is on black
            while l > LBLACK: 
                # Restates the color sensor values
                r = rline_sensor.reflection() 
                l = lline_sensor.reflection()
                leftdrive.run(-50)
            leftdrive.stop()
            break
        
        # If both sensors sense black at the same time, it just stops
        if r <= RBLACK and l <= LBLACK: 
            break