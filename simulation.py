from map import Map
from agent import Agent
from menu import Menu


class Simulation:

  def __init__(self):
    self.agents = []
    self.map = Map()

  def run(self):
    Menu(self).main()

  def set_random_agent(self):
    [x, y] = self.map.random_xy_zero()
    a = Agent(x, y)
    self.map.set_agent(x, y, a)
    self.agents.append(a)
