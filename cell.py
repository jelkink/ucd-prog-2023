class Cell:

  def __init__(self, simulation, x, y):
    self.agent = None
    self.simulation = simulation
    self.x = x
    self.y = y

  def is_empty(self):
    return self.agent == None

  def set_agent(self, agent):
    self.agent = agent

  def get_agent(self):
    if self.is_empty():
      self.simulation.error("Request for non-existing agent")
    
    return self.agent