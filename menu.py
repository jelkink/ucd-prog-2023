class Menu:

  def __init__(self, simulation):
    self.simulation = simulation

  def main(self):
    continue_menu = True
    while continue_menu:
      print("")
      print("MENU")
      print("")
      print("Set (s)ize of the map")
      print("Add number of (a)gents")
      print("(R)un a set number of iterations")
      print("(P)rint map")
      print("Print s(t)atistics")
      print("Plot (c)ounts")
      print("(Q)uit")
      print("")
      ans = input("Menu choice: ")

      if ans == "q" or ans == "Q":
        continue_menu = False
      elif ans == "s" or ans == "S":
        self.simulation.map.generate(self.map_size())
      elif ans == "r" or ans == "R":
        self.simulation.loop(self.iterations())
      elif ans == "a" or ans == "A":
        self.number_agents()
      elif ans == "p" or ans == "P":
        self.simulation.map.print()
      elif ans == "t" or ans == "T":
        self.simulation.print_statistics()
      elif ans == "c" or ans == "C":
        self.simulation.stats.plot()

  def map_size(self):
    N = input("How large should the map be (length of a square map): ")
    if not N.isnumeric():
      self.simulation.error("The map size should be a number")
      return 0

    N = int(N)
    if N < 1 or N > 100:
      self.simulation.error("Map size needs to be between 1 and 100")
      return 0

    return N

  def iterations(self):
    map_size = self.simulation.map.get_length()**2

    if map_size == 0:
      self.simulation.error("Cannot run simulation before setting the map size")
      return 0
      
    N = input("Enter the number of iterations to run: ")
    if not N.isnumeric():
      self.simulation.error("The number of iterations entered is not a number")
      return 0

    N = int(N)
    if N < 1:
      self.simulation.error("Number of iterations needs to be a positive number")
      return 0

    return N
  
  def number_agents(self):
    map_size = self.simulation.map.get_length()**2

    if map_size == 0:
      self.simulation.error("Cannot set number of agents before setting the map size")
      return 0

    ans = input("How many agents should there be: ")

    if not ans.isnumeric():
      self.simulation.error("The number of agents should be a number")
      return 0

    ans = int(ans)
    if ans < 1 or ans > map_size:
      self.simulation.error("The number of agents should be between 1 and %d" %
            map_size)
      return 0

    i = 0
    while i < ans:
      self.simulation.set_random_agent()
      i += 1

    self.simulation.log("Added {} agents".format(ans))
