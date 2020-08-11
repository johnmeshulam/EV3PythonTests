from util.run import Run
from functions import line
from util.robot import Robot

class Light_Cal(Run):

  def run(self):
      Robot.reset_light()