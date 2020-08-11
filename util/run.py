import input
from pybricks.parameters import Button

class Run():

  @staticmethod
  def running():
    return not(input.button(Button.DOWN) and input.button(Button.CENTER))

  def __init__(self, name): 
        self.name = name 

  def run(self):
    running = True
