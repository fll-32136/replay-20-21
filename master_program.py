#!/usr/bin/env pybricks-micropython
from pybricks.hubs import *
from math import *
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from run01 import *
from run02 import *
from run03 import *

ev3 = EV3Brick()

# This program is running forever so that you can 
# press the buttons at any time
while True: 
    # Calls buttons
    buttons = ev3.buttons.pressed()
    # If the up button is hit, it would run run 1
    if Button.UP in buttons: 
        run01_6()
    # If the right button is pressed it would run run 2
    elif Button.RIGHT in buttons: 
        run02()
    # If the down button is pressed it would run run 3
    elif Button.DOWN in buttons: 
        run03()