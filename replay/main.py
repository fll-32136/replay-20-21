#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

def straight(Speed, Time):
    motor = Motor(Port.A)
    motor1 = Motor(Port.B)
    wheel_diameter = 46
    axle_track = 114
    robot = DriveBase(motor, motor1, wheel_diameter, axle_track)
    robot.drive_time(Speed, 0, Time) #Time in seconds by thousands
    robot.stop(Stop.BRAKE)

def pivot_turn(direction, degrees):
    left_motor = Motor(Port.A)
    right_motor = Motor(Port.B)
    wheel_diameter = 56
    axle_track = 114
    robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
    robot.drive_time(math.pi * axle_track / 4, direction, degrees)
    robot.stop(Stop.BRAKE)

def turn(direction, degrees):
    motor = Motor(Port.A)
    motor1 = Motor(Port.B)
    wheel_diameter = 46
    axle_track = 114
    robot = DriveBase(motor, motor1, wheel_diameter, axle_track)
    robot.drive_time(0, direction, degrees)
    robot.stop(Stop.BRAKE)

def left_att(degrees, Speed):
    left_att_motor = Motor(Port.C)
    wheel_diameter = 46
    axle_track = 114
    left_att_move = DriveBase(left_att_motor, wheel_diameter, axle_track)
    left_att_move.drive_time(degrees, 0, Speed)
    left_att_move.stop(Stop.BRAKE)

def right_att(degrees, Speed):
    right_att_motor = Motor(Port.D)
    wheel_diameter = 46
    axle_track = 114
    right_att_move = DriveBase(right_att_motor, wheel_diameter, axle_track)
    right_att_move.drive_time(degrees, 0, Speed)
    right_att_move.stop(Stop.BRAKE)

# Step Counter Program
# right_att(360, 1000)
# left_att(360, 1000)
# straight(1000, 1750)
# straight(25, 9000)

# Run 3
straight(100, 2000)
turn(-90, 75)
straight(100, 500)
right_att(360, 100)
straight(-100, 1000)
turn(90, 135)
straight(100, 250)
turn(90, 90)
straight(100, 3500)
turn(-90, 90)