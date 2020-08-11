from robot import Robot
from pybricks.parameters import Button
from pybricks.tools import wait

def align(drive_speed, align_speed):
  forgiveness = 5
  black = Robot.black + forgiveness

  right_value, left_value = robot.get_light()

  if(not on_line):
    Robot.chassis.drive(drive_speed, 0)
    while(not on_line):
      right_value, left_value = robot.get_light()
    Robot.chassis.stop()
    Robot.brake()

  if(not aligned):
    if(right_value <= black):
      Robot.wheel_left.run(align_speed)
    elif(left_value <= black):
      Robot.wheel_right.run(align_speed)

    while(not aligned):
      right_value, left_value = robot.get_light()
      Robot.brick.screen.print(left_value, right_value)  

  Robot.brake()

def on_line(black):
  return right_value <= black or left_value <= black

def aligned(black):
  return right_value <= black and left_value <= black

#for higher versions - create side enum and pass is instead of sensor, add line side parameter
def follow_distance(distance, sensor, speed, kp):
  Robot.chassis.reset()
  target = (Robot.black + Robot.white) / 2

  while Robot.chassis.distance() < distance:
    error = sensor.reflection() - target
    turn = error * kp
    Robot.brick.screen.print(Robot.chassis.distance())
    Robot.chassis.drive(speed, turn)

    wait(10)

  
  Robot.brake()
