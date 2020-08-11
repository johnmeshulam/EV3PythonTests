#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Button
import pybricks.tools as tools
from pybricks.media.ev3dev import Font
from util.robot import Robot
import util.input as input
from runs import run1, light_cal

def display_menu():
  Robot.brick.screen.clear()
  Robot.brick.screen.print(" ^ " + run1.name)
  Robot.brick.screen.print(" > " + light_cal.name)
  #Robot.brick.screen.print(" v " + .name)
  #Robot.brick.screen.print(" < " + .name)
  #Robot.brick.screen.print("[] " + .name)

while True:
  display_menu()
  pressed = Robot.brick.buttons.pressed()

  btn = input.wait_for_any_press()
  print(btn)

  if(btn==Button.UP):
    pass
    run1.start()
  elif(btn==Button.RIGHT):
    pass
    light_cal.start()
  elif(btn==Button.DOWN):
    pass
  elif(btn==Button.LEFT):
    pass
  elif(btn==Button.CENTER):
    pass

    

    


