from map import Map
from agent import Agent
from menu import Menu
from log import Log
from configuration import Configuration

import random


class Simulation:

  def __init__(self):
    self.agents = []
    self.map = Map(self)
    self.time = 0
    self.log_ = Log("simulation.log")
    self.config = Configuration()

  def run(self):
    Menu(self).main()

  def loop(self, iterations):
    self.log(f"Starting run of {iterations} iterations")
    for i in range(iterations):
      
      for j in range(self.config.immigration_rate):
        self.set_random_agent()
        
      for a in self.agents:
        a.reset_ptr()

      for a in self.agents:
        a.interaction()
      
      self.time += 1

  def set_random_agent(self):
    [x, y] = self.map.random_xy_zero()
    strategy = random.choice(["altruist", "ethnocentric", "cosmopolitan", "egoist"])
    group = random.randint(1, self.config.number_of_groups)
    a = Agent(self, x, y, strategy, self.config.base_ptr, group)
    self.map.set_agent(x, y, a)
    self.agents.append(a)

  def log(self, text):
    self.log_.write("[%05d] " % self.time + text)
  
  def error(self, text):
    self.log_.write("[%05d] " % self.time + "ERROR: " + text)
    print("ERROR: " + text)

  def get_map(self):
    return self.map