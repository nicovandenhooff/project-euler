# Project Euler: Problem 19
# Counting Sundays
# Author: Nico Van den Hooff
# Github: https://github.com/nicovandenhooff/project-euler
# Problem: https://projecteuler.net/problem=19

# This problem is easy to solve with pandas.  I opt to keep it simple
# here and not create a function due to the specificity of the question.

import pandas as pd

# create range of Sundays
sundays = pd.date_range(start="19010101", end="20001231", freq="W-SUN")

# filter for only first of month
firsts = sundays[sundays.day == 1]

print(len(firsts))
