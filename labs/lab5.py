# BEGIN: code from Lab 4

import math
import random

def generate_map(N):
  L = []
  i = 0
  while i < (N * N):
    L.append(0)
    i += 1
  return L

def get_index(x, y, N):
  if x > N or x < 1 or y > N or y < 1:
    print("ERROR: (x,y) coordinates outside the map boundaries!")
  return (x-1) * N + (y-1)

def get_value(x, y, L, change = False):
  N = int(math.sqrt(len(L)))
  if change:
    L[get_index(x, y, N)] = 1 - L[get_index(x, y, N)]
  return L[get_index(x, y, N)]

def random_xy_zero(L):
  N = int(math.sqrt(len(L)))

  found = False
  x = 1
  while x <= N and not found:
    y = 1
    while y <= N and not found:
      if get_value(x, y, L) == 0:
        found = True
      y += 1
    x += 1

  if not found:
    print("ERROR: No empty cells available!")
    return None
  
  x = random.randint(1, N)
  y = random.randint(1, N)
  while get_value(x, y, L) == 1:
    x = random.randint(1, N)
    y = random.randint(1, N)
  return [x, y]
  
def set_random_agent(A, L):
  [x,y] = random_xy_zero(L)
  get_value(x, y, L, True)
  A.append({"x": x, "y": y})

# END: code from Lab 4
  
def menu_map_size():
  N = input("How large should the map be (length of a square map): ")
  if not N.isnumeric():
    print("ERROR: The map size should be a number")
    return 0

  N = int(N)
  if N < 1 or N > 100:
    print("ERROR: Map size needs to be between 1 and 100")
    return 0
    
  return N

def menu_number_agents(agents, map):
  if len(map) == 0:
    print("ERROR: Cannot set number of agents before setting the map size")
    return 0
  
  ans = input("How many agents should there be: ")
  
  if not ans.isnumeric():
    print("ERROR: The number of agents should be a number")
    return 0

  ans = int(ans)
  if ans < 1 or ans > len(map):
    print("ERROR: The number of agents should be between 1 and %d" % len(map))
    return 0

  agents = []
  i = 0
  while i < ans:
    set_random_agent(agents, map)
    i += 1

def print_map(map):
  N = int(math.sqrt(len(map)))
  x = 1
  while x <= N:
    y = 1
    while y <= N:
      if get_value(x, y, map) == 0:
        print("-", end = "")
      else:
        print("X", end = "")
      y += 1
    print("")
    x += 1

def menu():
  map = []
  agents = []
  
  continue_menu = True
  while continue_menu:
    print("")
    print("MENU")
    print("")
    print("Set (s)ize of the map")
    print("Add number of (a)gents")
    print("(P)rint map")
    print("(Q)uit")
    print("")
    ans = input("Menu choice: ")

    if ans == "q" or ans == "Q":
      continue_menu = False
    elif ans == "s" or ans == "S":
      map = generate_map(menu_map_size())
    elif ans == "a" or ans == "A":
      menu_number_agents(agents, map)
    elif ans == "p" or ans == "P":
      print_map(map)

# Some notes to keep in mind:
# 
# "generate map" was removed, as the map is already generated when parameters are entered
# "set number of agents" actually adds the number of agents; if there are agents already, they are not removed
#
# Many different decisions could have been made, e.g. there is a decision here
# for the menu function to not save the number of agents or the map size,
# but only the lists
