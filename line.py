from robot import Robot

black = 10 #needs to be calibrated

def align(drive_speed, align_speed):
  right_value, left_value, on_line, aligned = calc_line()

  if(not on_line):
    Robot.chassis.drive(drive_speed, 0)
    while(not on_line):
      right_value, left_value, on_line, aligned = calc_line()
    Robot.chassis.stop()
    Robot.brake()
      
  if(not aligned):
    if(right_value < black):
      Robot.wheel_left.run(align_speed)
    elif(left_value < black):
      Robot.wheel_right.run(align_speed)

    while(not aligned):
      right_value, left_value, on_line, aligned = calc_line()
      Robot.brick.screen.print(left_value, right_value)      
    Robot.brake()

def calc_line():
  right_value = Robot.color_right.reflection()
  left_value = Robot.color_left.reflection()

  on_line = right_value < black or left_value < black
  aligned = right_value < black and left_value < black

  return (right_value, left_value, on_line, aligned)