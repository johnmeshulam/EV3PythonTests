from robot import Robot

  black = 10 #needs to be calibrated

  def align(drive_speed, align_speed):
    right_value, left_value, on_line, aligned = calc_line()

    if(not on_line):
      robot.chassis.drive(drive_speed, 0)
      while(not on_line):
        right_value, left_value, on_line, aligned = calc_line()
      robot.chassis.stop()
      robot.brake()
        
    if(not aligned):
      if(right_value < black):
        robot.wheel_left.run(align_speed)
      elif(left_value < black):
        robot.wheel_right.run(align_speed)

      while(not aligned):
        right_value, left_value, on_line, aligned = calc_line()
        robot.brick.screen.print(left_value, right_value)      
      robot.brake()

  def calc_line():
    right_value = robot.color_right.reflection()
    reft_value = robot.color_left.reflection()

    on_line = right_value < black or left_value < black
    aligned = right_value < black and left_value < black

    return (right_value, left_value, on_line, aligned)