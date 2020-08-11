from pybricks.parameters import Button
from util.robot import Robot
import time

lastPressed = {
  Button.UP: time.time(),
  Button.RIGHT: time.time(),
  Button.DOWN: time.time(),
  Button.LEFT: time.time(),
  Button.CENTER: time.time()
}
press_time = 0.7

def button(btn):
  return btn in Robot.brick.buttons.pressed()

def button_down(btn, refreshTime = 0.35):
  if(lastPressed[btn] + refreshTime <= time.time()):
    lastPressed[btn] = time.time()
    return button(btn)

  return False

def wait_for_press(btn):
  while(not button(btn)):
    pass
  while(button(btn)):
    pass

def wait_for_any_press():
  while(len(Robot.brick.buttons.pressed()) == 0):
    pass

  start_time = time.time()
  btn = Robot.brick.buttons.pressed()[0]

  while(len(Robot.brick.buttons.pressed()) > 0):
    pass

  if(time.time() >= start_time + press_time):
    return None

  return btn