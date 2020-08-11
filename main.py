#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Button
import pybricks.tools as tools
from util import buttons
from util.robot import Robot
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

  btn = buttons.wait_for_any_press()
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

    

    


