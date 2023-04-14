from datetime import datetime


class Log:

  def __init__(self, filename):
    self.filename = filename

  def write(self, event):
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open(self.filename, "a") as log:
      log.write(now + " " + event + "\n")

  def read(self):
    with open(self.filename, "r") as log:
      print(log.read())

  def clear(self):
    open(self.filename, "w")
