from robot import Robot
from pybricks.parameters import Button
from pybricks.tools import wait

def turn_to(target, turn_speed):
  while not Robot.gyro.angle() == target:
    direction = 1
    if(target < Robot.gyro.angle()):
      direction = -1
    turn = turn_speed * direction

    Robot.brick.screen.print(Robot.gyro.angle())
    Robot.chassis.drive(0, turn)

    wait(10)
  
  Robot.brake()


#for higher levels - thin about merging this with line.follow and allowing for follow method switching
#you know, since the difference between the methods is literally two lines
def follow_distance(distance, target, speed, kp):
  Robot.chassis.reset()

  while Robot.chassis.distance() < distance:
    error = target - Robot.gyro.angle()
    turn = error * kp
    Robot.brick.screen.print(Robot.gyro.angle())
    Robot.chassis.drive(speed, turn)

    wait(10)

  
  Robot.brake()
