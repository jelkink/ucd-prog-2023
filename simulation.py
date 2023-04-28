from map import Map
from agent import Agent
from menu import Menu
from log import Log
from configuration import Configuration
from stats import Stats

import random


class Simulation:

  def __init__(self):
    self.agents = []
    self.map = Map(self)
    self.time = 0
    self.log_ = Log("simulation.log")
    self.config = Configuration()
    self.stats = Stats(self)

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

      shuffled_agents = random.sample(self.agents, len(self.agents))
      for a in shuffled_agents:
        a.reproduce()

      for a in self.agents:
        a.die()

      self.stats.update()

      self.time += 1

  def set_random_agent(self):
    [x, y] = self.map.random_xy_zero()
    cell = self.map.get_cell(x, y)
    strategy = random.choice(["altruist", "ethnocentric", "cosmopolitan", "egoist"])
    group = random.randint(1, self.config.number_of_groups)
    a = Agent(self, cell, strategy, self.config.base_ptr, group)
    cell.set_agent(a)
    self.agents.append(a)

  def calculate_statistics(self):
    count_strategy = {'altruist': 0, 'ethnocentric': 0, 'cosmopolitan': 0, 'egoist': 0}
    
    for a in self.agents:
      count_strategy[a.get_strategy()] += 1

    return count_strategy

  def print_statistics(self):

    count_strategy = self.calculate_statistics()

    print(f"Altruists: {count_strategy['altruist']}, Ethnocentrists: {count_strategy['ethnocentric']}, Cosmopolitans: {count_strategy['cosmopolitan']}, and Egoists: {count_strategy['egoist']}")
  
  def log(self, text):
    self.log_.write("[%05d] " % self.time + text)
  
  def error(self, text):
    self.log_.write("[%05d] " % self.time + "ERROR: " + text)
    print("ERROR: " + text)

  def get_map(self):
    return self.map

  def get_config(self):
    return self.config