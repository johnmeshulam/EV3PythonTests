from util import line, gyro
from util.robot import Robot


name = "gyro turn"

def start():
  Robot.reset_gyro()
  gyro.turn_to(90, 40)