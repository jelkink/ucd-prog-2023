class Agent:

  def __init__(self, simulation, x, y, strategy, ptr, group):
    self.simulation = simulation
    self.x = x
    self.y = y
    self.strategy = strategy
    self.ptr = ptr
    self.base_ptr = ptr
    self.group = group

  def reset_ptr(self):
    self.ptr = self.base_ptr
  
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

  def is_cooperate(self, other):
    if self.strategy == "altruist":
      return True
    elif self.strategy == "cosmopolitan" and other.group != self.group:
      return True
    elif self.strategy == "ethnocentric" and other.group == self.group:
      return True
    else:
      return False

  def prisoner_dilemma(self, other):
    if self.is_cooperate(other):
      self.ptr -= .01
    if not other.is_cooperate(self):
      self.ptr -= .03

  def interaction(self):
    others = self.get_neighbours()

    for a in others:
      self.prisoner_dilemma(a)

  def get_neighbours(self):
    coords_neighbours = self.simulation.get_map().get_neighbour_coordinates(self.x, self.y)

    neighbours = []
    for coords in coords_neighbours:
      cell = self.simulation.get_map().get_cell(coords[0], coords[1])
      if not cell.is_empty():
        neighbours.append(cell.get_agent())

    return neighbours