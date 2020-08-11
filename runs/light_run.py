from util import line, gyro
from robot import Robot

name = "line follow"

def start():
  Robot.reset_gyro()
  gyro.follow_distance(500, 0, 70, 1.5)