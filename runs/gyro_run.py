from util import line, gyro
from robot import Robot


name = "gyro turn"

def start():
  Robot.reset_gyro()
  gyro.turn_to(90, 40)