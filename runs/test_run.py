from util import line, gyro
from util.robot import Robot
from pybricks.tools import wait

name = "test run"

def start():
  Robot.reset_gyro()
  Robot.arm_left.run_angle(-600, 700, wait = False)
  line.follow_distance(380, Robot.color_right, 120, 1.5)
  wait(10)
  gyro.follow_distance(80, 15, 60, 0.5)
  wait(10)
  Robot.brick.screen.print("finished gyro follow")
  Robot.arm_left.run_angle(600, 700)
  Robot.brick.screen.print("finished close arm")