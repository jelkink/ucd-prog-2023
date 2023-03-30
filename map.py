import random
import math

from cell import Cell


class Map:

  def __init__(self):
    self.cells = []

  def generate(self, N):
    self.cells = []
    i = 0
    while i < (N * N):
      self.cells.append(Cell())
      i += 1

  def get_cell(self, x, y):
    return self.cells[self.get_index(x, y)]

  def set_agent(self, x, y, agent):
    self.cells[self.get_index(x, y)].set_agent(agent)

  def get_length(self):
    return int(math.sqrt(len(self.cells)))

  def get_index(self, x, y):
    N = self.get_length()
    if x > N or x < 1 or y > N or y < 1:
      print("ERROR: (x,y) coordinates outside the map boundaries!")
    return (x - 1) * N + (y - 1)

  def random_xy_zero(self):
    N = self.get_length()
    found = False
    x = 1
    while x <= N and not found:
      y = 1
      while y <= N and not found:
        if self.get_cell(x, y).is_empty():
          found = True
        y += 1
      x += 1

    if not found:
      print("ERROR: No empty cells available!")
      return None

    x = random.randint(1, N)
    y = random.randint(1, N)
    while not self.get_cell(x, y).is_empty():
      x = random.randint(1, N)
      y = random.randint(1, N)
    return [x, y]

    # The above is probably not the most efficient;
    # might be better to keep a separate list of all
    # the empty cells, then you can immediately check
    # the list length and randomly pick one.

  def print(self):
    N = self.get_length()
    x = 1
    while x <= N:
      y = 1
      while y <= N:
        if self.get_cell(x, y).is_empty():
          print("-", end="")
        else:
          print("X", end="")
        y += 1
      print("")
      x += 1
