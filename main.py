#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Button
import pybricks.tools as tools
from util.robot import Robot
import util.input as input
from runs.run1 import Run1
from runs.light_cal import Light_Cal


runs = [Run1("line align"), Light_Cal("reset light"), Run1("test2"), Run1("test3"), Run1("test4"), Run1("test5")]
current_run = None
index = 0

def display_menu():
  Robot.brick.screen.clear()
  i = 0
  prefix = " "
  for run in runs:
    if(i == index):
      prefix = ">"
    else:
      prefix = " "

    Robot.brick.screen.draw_text(0, i * 20, prefix + run.name)
    i += 1

while True:
  display_menu()
  pressed = Robot.brick.buttons.pressed()

  btn = input.wait_for_any_press()
  print(btn)
  if(btn==Button.DOWN and index < len(runs) - 1):
    index += 1
    print(index)
  elif(btn==Button.UP and index > 0):
    index -= 1
    print(index)
  elif(btn==Button.CENTER):
    Robot.brick.screen.clear()
    runs[index].run()
    tools.wait(700)

    

    


