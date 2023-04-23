class Agent:

  def __init__(self, x, y, strategy):
    self.x = x
    self.y = y
    self.strategy = strategy

  def get_strategy(self):
    return self.strategy

  def get_strategy_code(self):
    if self.strategy == "altruist":
      return "A"
    elif self.strategy == "ethnocentric":
      return "E"
    elif self.strategy == "cosmopolitan":
      return "C"
    else:
      return "S"