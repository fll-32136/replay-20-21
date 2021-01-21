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
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

while True: #This program is running forever so that you can press the buttons at any time
    buttons = ev3.buttons.pressed()
    if Button.UP in buttons: #If the up button is hit, it would run run 1
        run01_6()
    elif Button.RIGHT in buttons: #If the right button is pressed it would run run 2
        run02()
    elif Button.DOWN in buttons: #If the down button is pressed it would run run 3
        run03()