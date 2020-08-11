from pybricks.parameters import Button
from robot import Robot
import time

lastPressed = {
  Button.UP: time.time(),
  Button.RIGHT: time.time(),
  Button.DOWN: time.time(),
  Button.LEFT: time.time(),
  Button.CENTER: time.time()
}

def button_down(button, refreshTime = 0.35):
  if(lastPressed[button] + refreshTime <= time.time()):
    lastPressed[button] = time.time()
    return button in Robot.brick.buttons.pressed()

  return False

def button(button):
  return button in Robot.brick.buttons.pressed()