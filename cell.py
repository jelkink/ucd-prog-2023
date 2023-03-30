class Cell:

  def __init__(self):
    self.agent = None

  def is_empty(self):
    return self.agent == None

  def set_agent(self, agent):
    self.agent = agent