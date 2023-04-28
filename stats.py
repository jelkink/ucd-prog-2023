class Stats:

  def __init__(self, simulation):
    self.egoists = []
    self.altruists = []
    self.cosmopolitans = []
    self.ethnocentrists = []
    self.simulation = simulation

  def update(self):

    counts = simulation.calculate_statistics()

    self.egoists.append(counts["egoist"])
    self.altruists.append(counts["altruist"])
    self.cosmopolitans.append(counts["cosmopolitan"])
    self.ethnocentrists.append(counts["ethnocentric"])

  def plot(self):
    pass