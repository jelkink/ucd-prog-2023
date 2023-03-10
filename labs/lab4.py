-# 2a. Write a function that takes a parameter N and returns a list of zeroes of length N * N.

def generate_list(N):
  L = []
  i = 0
  while i < (N * N):
    L.append(0)
    i += 1
  return L

print(generate_list(0))
print(generate_list(1))
print(generate_list(10))

# 2b. Write a function that takes as parameters an x and y value, and a list length N, and returns a list index as follows: i = (x-1) * N + (y-1).

def get_index(x, y, N):
  return (x-1) * N + (y-1)

print(get_index(1, 1, 5) == 0)
print(get_index(1, 5, 5) == 4)
print(get_index(3, 4, 5) == 13)

# 2b. Write a function that takes a parameter L, which is a list of ones and zeroes, and parameters x and y representing coordinates, which returns the value of that point in the list, using 2b. Note that N is the square root of the length of the list. Test using a list generated in 2a.

import math

def get_value(x, y, L):
  N = int(math.sqrt(len(L)))
  return L[get_index(x, y, N)]

print(get_value(3, 5, generate_list(5)))

# 2c. Modify the function in 2b to print an error message on the screen when x or y is not within the range 1 to n.

def get_index(x, y, N):
  if x > N or x < 1 or y > N or y < 1:
    print("ERROR: (x,y) coordinates outside the map boundaries!")
  return (x-1) * N + (y-1)

print(get_index(1, 1, 5) == 0)
print(get_index(1, 5, 5) == 4)
print(get_index(3, 4, 5) == 13)
print(get_index(8, 2, 5))

# 2d. Modify the function in 2d to take an additional boolean parameter, which if set, changes the value at the point in the list at (x,y). The default value of the parameter should be False, so that if you do not use it, it will by default not change the data.

def get_value(x, y, L, change = False):
  N = int(math.sqrt(len(L)))
  if change:
    L[get_index(x, y, N)] = 1 - L[get_index(x, y, N)]
  return L[get_index(x, y, N)]

test_list = generate_list(5)
print(get_value(3, 5, test_list))
print(get_value(3, 5, test_list, True))
print(get_value(3, 5, test_list))
print(test_list)

# 3a. Write a function that takes a list and returns random x and y coordinates. The x and y coordinates have to be valid, given the length of the list.

import random

def random_xy(L):
  N = int(math.sqrt(len(L)))
  return [random.randint(1, N), random.randint(1, N)]

print(random_xy(test_list))
print(random_xy(test_list))
print(random_xy(test_list))

# 3b. Write a modification of 3a, returning only coordinates for a cell that has a zero value.

def random_xy_zero(L):
  N = int(math.sqrt(len(L)))
  x = random.randint(1, N)
  y = random.randint(1, N)
  while get_value(x, y, L) == 1:
    x = random.randint(1, N)
    y = random.randint(1, N)
  return [x, y]

# BEWARE: the above function creates an endless loop if there are no empty cells!

# this is not part of the exercise, but just to create a bit of a test, we 
# create a map where the first three rows is always 1, so we should not get
# random locations in that area:
test_list = generate_list(5)

x = 1
while x <= 3:
  y = 1
  while y <= 5:
    get_value(x, y, test_list, True)
    y += 1
  x += 1

print(test_list)

print(random_xy_zero(test_list))
print(random_xy_zero(test_list))
print(random_xy_zero(test_list))

# Expanded version that is slower, but safer:
# Note how it is constructed in such a way, that once an empty cell is found,
# the search ends, so we do not search the entire map even when we already know
# there is at least one empty cell.

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
  
print(random_xy_zero(test_list))
print(random_xy_zero(test_list))
print(random_xy_zero(test_list))

# 4. Using all of the above, write a function that takes a list A, a list L, then finds a random position that is 0 in L, sets it to 1, and adds the (x,y) coordinates to A. A should be a list of dictionaries, where every item has a value "x" and a value "y".

def set_random_agent(A, L):
  [x,y] = random_xy_zero(L)
  get_value(x, y, L, True)
  A.append({"x": x, "y": y})

agents = []
map = generate_list(5)

print(map)
print(agents)
set_random_agent(agents, map)
print(map)
print(agents)
set_random_agent(agents, map)
print(map)
print(agents)
set_random_agent(agents, map)
print(map)
print(agents)