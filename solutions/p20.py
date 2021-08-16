# Project Euler: Problem 20
# Factorial digit sum
# Author: Nico Van den Hooff
# Github: https://github.com/nicovandenhooff/project-euler
# Problem: https://projecteuler.net/problem=20

import math

print(sum([int(num) for num in str(math.factorial(100))]))
