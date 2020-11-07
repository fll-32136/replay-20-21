#!/usr/bin/env pybricks-micropython
from pybricks.hubs import *
from math import *
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from run02 import *
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


stepcounter()

# Step Counter Program
# right_att(360, 1000)
# left_att(360, 1000)
# straight(1000, 1750)
# straight(25, 9000)

#  Run 3
# straight(100, 2000)
# turn(-90, 75)
# straight(100, 500)
# right_att(360, 100)
# straight(-100, 1000)
# turn(90, 135)
# straight(100, 250)
# turn(90, 90)
# straight(100, 3500)
# turn(-90, 90)