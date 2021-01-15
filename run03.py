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
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

right_motor = Motor(Port.A)
left_motor = Motor(Port.B) 
wheel_diameter = 56 
axle_track = 114
straight_robot = DriveBase(right_motor, left_motor, wheel_diameter, axle_track)
# Create your objects here.
ev3 = EV3Brick()
gyro_sensor = GyroSensor(Port.S4)
leftcolorsensor=ColorSensor(Port.S3)
rightcolorsensor=ColorSensor(Port.S1)
BLACK=5
WHITE=55

# Alignment: Right wheel on 6th line with robot on back wall
# Attachment start position 2 cubes at the top

# def gyro_finder():
#     gyro_sensor = GyroSensor(Port.S4)
#     print(gyro_sensor.angle())

# left_motor = Motor(Port.B)
# right_motor = Motor(Port.A)

# robot = DriveBase(left_motor, right_motor, wheel_diameter=46, axle_track=114)

# def gyro_stop(gyro_num):   
#     gyro_sensor = GyroSensor(Port.S4)
#     gyro_sensor.reset_angle(0)
#     while gyro_sensor.angle() != gyro_num:
#         if gyro_sensor.angle() < gyro_num:
#             robot.drive(50,20)
#         elif gyro_sensor.angle() > gyro_num:
#             robot.drive(50,-20)

def run03():
    straight(400, 1550)
    # robot.settings(0, 0, 100, 100)
    # robot.turn(-12.5)
    turn(-90, 175)
    time.sleep(1)
    # Negative speed makes attachment move 
    left_att(3000, -2000)
    straight(-1000, 1250)
    turn(-90, 230)
    straight(400, 1800)
    line_square(8,5,70)
    straight(400, 400)
    turn(90, 950)
    straight(-200, 1500)
    straight_robot.drive(-200, 0)
    colorstop(straight_robot, rightcolorsensor, 8)
    pivot_turn(-90, 600)
    straight(300, 550)
    right_att(650, -200)
    time.sleep(0.5)
    straight(-300, 500)
    turn(90, 500)
    straight(400, 1300)
    turn(90, 700)
    straight(-100, 1500)
    while True:
        straight(-100, 800)
        straight(100, 600)
# run03()

    # straight(100, 3550)
    # # robot.settings(0, 0, 100, 100)
    # # robot.turn(-12.5)
    # turn(-90, 175)
    # time.sleep(1)
    # # Negative speed makes attachment move 
    # left_att(4000, -2000)
    # straight(-100, 900)
    # turn(-90, 420)
    # straight(1000, 3600)
    # turn(90, 700)
    # straight(100, 600)
    # turn(90, 300)
    # straight(-100, 550)
    # turn(-90, 200)
    # straight(100, 400)
    # right_att(650, -200)
    # time.sleep(3)
    # straight(-300, 500)
    # turn(90, 600)
    # straight(100, 2500)
    # turn(90, 600)
    # straight(-100, 1500)
    # while True:
    #     straight(-100, 800)
    #     straight(100, 600)