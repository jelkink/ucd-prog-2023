# 1. Write a function that accepts an integer (n) and computes the value of n + nn + nnn. (nn means n times n.)

def n_nn_nnn(n):
  return(n + n * n + n * n * n)

print(n_nn_nnn(-1))
print(n_nn_nnn(0))
print(n_nn_nnn(1))
print(n_nn_nnn(5))

# a good habit is to start writing tests, e.g. these all should print "true" or I did something wrong:

print(n_nn_nnn(-1) == -1)
print(n_nn_nnn(0) == 0)
print(n_nn_nnn(1) == 3)
print(n_nn_nnn(2) == 14)

# 2a. Write a function that has as input parameter "guess" a guessed dice value, then throws a dice, and returns the difference between the thrown value and the guessed value.

import random

def check_guess(guess):
  return(random.randint(1, 6) - guess)

print(check_guess(3))
print(check_guess(-1))
print(check_guess(0))
print(check_guess(7))

# 2b. Change the above function to guess the sum of three throws instead.

def check_guess_3(guess):
  throw1 = random.randint(1, 6)
  throw2 = random.randint(1, 6)
  throw3 = random.randint(1, 6)
  return(throw1 + throw2 + throw3 - guess)

print(check_guess_3(3))
print(check_guess_3(-1))
print(check_guess_3(0))
print(check_guess_3(7))

# 2c. Write a function dice() that takes as input parameter the number of sides of the dice and returns a random dice throw. Edit the functions from 2a and 2b to use this function instead.

# 3. Write a function that accepts the radius of a circle as input and computes the area.

# 4. Take or rewrite the function that returns the Euclidean distance between two points.

# 5. Write a function that takes a first and last name as input and returns them in reverse order, with the last name in capitals.