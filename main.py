#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Button
import pybricks.tools as tools
from util import buttons
from util.robot import Robot
from runs import gyro_run, light_run, light_cal

def display_menu():
  Robot.brick.screen.clear()
  Robot.brick.screen.print(" ^ " + light_run.name)
  Robot.brick.screen.print(" > " + gyro_run.name)
  Robot.brick.screen.print(" v " + light_cal.name)
  #Robot.brick.screen.print(" < " + .name)
  #Robot.brick.screen.print("[] " + .name)

while True:
  display_menu()

  btn = buttons.wait_for_any_press()
  print(btn)

  if(btn==Button.UP):
    light_run.start()
    pass
  elif(btn==Button.RIGHT):
    gyro_run.start()
    pass
  elif(btn==Button.DOWN):
    light_cal.start()
    pass
  elif(btn==Button.LEFT):
    #your run here
    pass
  elif(btn==Button.CENTER):
    #your run here
    pass

    

    


