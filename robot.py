class Robot:

  brick = EV3Brick()

  wheel_left = Motor(Port.B)
  wheel_right = Motor(Port.C)

  gyro = GyroSensor(Port.S1, Direction.COUNTERCLOCKWISE)
  color_left = ColorSensor(Port.S2)
  color_right = ColorSensor(Port.S4)

  chassis = DriveBase(wheel_left, wheel_right, wheel_diameter=62.4, axle_track=100)

  @classmethod
  def brake(cls):
    cls.chassis.stop()
    cls.wheel_left.brake()
    cls.wheel_right.brake()
    
  @classmethod
  def reset_gyro(cls):
    gyro.angle()
    gyro.speed()
  +  gyro.angle()