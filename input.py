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

refreshTime = 0.25

def button_down(button):
  print(lastPressed[button], time.time())
  if(lastPressed[button] + refreshTime <= time.time()):
    lastPressed[button] = time.time()
    return button in Robot.brick.buttons.pressed()

  return False