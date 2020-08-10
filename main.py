#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Button
from robot import Robot
from runs.run1 import Run1
import input

runs = [Run1("line align"), Run1("test"), Run1("test2"), Run1("test3"), Run1("test4"), Run1("test5")]
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

def display_running():
  Robot.brick.screen.clear()
  Robot.brick.screen.draw_text(0, 0, "Currently Running ")
  Robot.brick.screen.draw_text(0, 20, runs[index].name + "...")

while True:
  display_menu()
  pressed = Robot.brick.buttons.pressed()

  while(len(pressed) == 0):
    pressed = Robot.brick.buttons.pressed()

  if(input.button_down(Button.DOWN) and index < len(runs) - 1):
    index += 1
    print(index)
  elif(input.button_down(Button.UP) and index > 0):
    index -= 1
    print(index)
  elif(input.button_down(Button.CENTER)):
    display_running()
    runs[index].run()






