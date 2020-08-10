#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Button
from robot import Robot
import line

while True:
  while(Button.CENTER not in Robot.brick.buttons.pressed()):
    pass

  line.align(100, 70)


