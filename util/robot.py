from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor, ColorSensor
from pybricks.parameters import Port, Direction, Button
from pybricks.robotics import DriveBase
from util import buttons
class Robot():

  #robot hardware
  brick = EV3Brick()

  wheel_left = Motor(Port.B)
  wheel_right = Motor(Port.C)

  gyro = GyroSensor(Port.S1, Direction.COUNTERCLOCKWISE)
  color_left = ColorSensor(Port.S2)
  color_right = ColorSensor(Port.S4)

  chassis = DriveBase(wheel_left, wheel_right, wheel_diameter=62.4, axle_track=100)

  #robot parameters
  black = 10
  white = 70
 
  @classmethod
  def brake(cls):
    cls.chassis.stop()
    cls.wheel_left.brake()
    cls.wheel_right.brake()

  @classmethod
  def reset_gyro(cls):
    cls.gyro.angle()
    cls.gyro.speed()
    cls.gyro.angle()

    cls.gyro.reset_angle(0)

  @classmethod
  def reset_light(cls):
    cls.brick.screen.clear()

    cls.brick.screen.draw_text(0, 0, "reset black")
    buttons.wait_for_press(Button.CENTER)
    cls.black = cls.color_left.reflection()

    cls.brick.screen.draw_text(120, 0, str(cls.black))
    cls.brick.screen.draw_text(0, 20, "reset white")
    buttons.wait_for_press(Button.CENTER)
    cls.white = cls.color_left.reflection()

    cls.brick.screen.draw_text(120, 20, str(cls.white))
    buttons.wait_for_press(Button.CENTER)