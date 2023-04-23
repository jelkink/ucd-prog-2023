from map import Map
from agent import Agent
from menu import Menu
from log import Log

import random


class Simulation:

  def __init__(self):
    self.agents = []
    self.map = Map(self)
    self.time = 0
    self.log_ = Log("simulation.log")

  def run(self):
    Menu(self).main()

  def loop(self, iterations):
    self.log("Starting run of {iterations} iterations")
    for i in range(iterations):
      self.set_random_agent()
      self.time += 1

  def set_random_agent(self):
    [x, y] = self.map.random_xy_zero()
    strategy = random.choice(["altruist", "ethnocentric", "cosmopolitan", "egoist"])
    a = Agent(x, y, strategy)
    self.map.set_agent(x, y, a)
    self.agents.append(a)

  def get_log(self):
    return self.log_

  def log(self, text):
    self.log_.write(text)
  
  def error(self, text):
    self.log_.write("ERROR: " + text)
    print("ERROR: " + text)