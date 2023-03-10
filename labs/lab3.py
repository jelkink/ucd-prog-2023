# 1a. Write a function with parameter N, that throws N dice and returns the sum.

import random

def diceSum(N):
  i = 0
  sum = 0
  while i < N:
    sum += random.randint(1, 6)
    i += 1
  return(sum)

# 1b. Write a function with parameters N and K, that, using the previous function, throws N dice and returns True when the sum is equal to K.

def checkSum(N, K):
  return(diceSum(N) == K)
  
# 1b. Write a function with parameters N, R, and K, using the previous function, that throws N dice R times and returns what proportion of results the sum of the N dice is exactly K.

def checkSumProp(N, R, K):
  i = 0
  countHits = 0
  while i < R:
    if checkSum(N, K):
      countHits += 1
    i += 1
  return(countHits / R)

# 2a. Write a simulation that calculates the number of infections after 100 time periods, when you start with 1 infected person, with each time step, for each infected person, a 15% chance of being cured, and a 25% chance of infecting one new person.

def simulation100():
  i = 0
  infected = 1
  while i < 100:
    new_infected = infected
    j = 0
    while j < infected:
      if random.random() < 0.25:
        new_infected += 1
      if random.random() < 0.15:
        new_infected -= 1
      j += 1
    infected = new_infected
    i += 1
  return(infected)
  
# 2b. Write a function that takes parameters N_start, N_times, P_infection and P_cure, representing the number of infected persons at the start, the number of time steps, the chance of infecting another person in each time step, and the chance of being cured in each time step, and that returns the number of infected persons at the end of the simulation.

def simulation(N_start, N_times, P_infect, P_cure):
  i = 0
  infected = N_start
  while i < N_times:
    new_infected = infected
    j = 0
    while j < infected:
      if random.random() < P_infect:
        new_infected += 1
      if random.random() < P_cure:
        new_infected -= 1
      j += 1
    infected = new_infected
    i += 1
  return(infected)

  
# 2c. Run the above simulation 20 times, with each time N_start=2, N_times=100, P_infection=0.25, P_cure=0.10. Experiment with different values to see results.

i = 0
while i < 20:
  print(simulation(2, 100, .25, .1))