# Project Euler: Problem 493
# Under The Rainbow
# Author: Nico Van den Hooff
# Github: https://github.com/nicovandenhooff/project-euler
# Problem: https://projecteuler.net/problem=793
#
# This problem can be solved by breaking it down into the following steps:
#   1) For each colour i, let Ii be the indicator random varible that
#      indicates whether or not that colour has been chosen.  If the
#      colour is chosen, Ii = 1, if it is not Ii = 0.  As we have 7
#      colours, we will have seven indicator random variables:
#      I1, I2, ... I7.
#   2) Let X be the random variable that represents the number of
#      distinct colours chosen in our sample, and E(X) be the
#      expected number of distinct colours.
#   3) Trying to solve for E(X) directly would be a disaster, but if
#      we think carefully, we can see that solving for E(X) is the same
#      thing as solving for E(I1 + I2 + ... + I7).
#   4) Since expectation is linear, the above is then the same as
#      solving for E(I1) + E(I2) + ... + E(I7).
#   5) Since we have the same number of balls for each colour, each
#      E(Ii) above will be equal, and the problem reduces even further
#      to solving for any of the E(Ii)'s and then multiplying it by 7.
#   6) For concreteness, let's focus on E(I1), and let colour 1 equal
#      red.  By the fundamental bridge of probability, finding E(I1)
#      is the same thing as finding P(Red Ball is Chosen).
#   7) Finding P(Red Ball is Chosen) is the same thing as finding
#      1 - P(No Red Ball is Chosen), which is easier to compute.
#   8) Since we have 70 balls, of which 10 are red and 60 are another
#      colour,P(No Red Ball is Chosen) can be calculated as 60 choose 20
#      divided by 70 choose 20.  There are 60 non-red balls, of which
#      we need to select 20, and there are 70 total balls, of which we
#      make a total of 20 choices
#   9) Finally we subtract the above from 1 and get our answer.
#
# Given the long explanation above, I opted to simply solve the
# problem below rather than defining a function as in my other
# Project Euler files.


from math import comb

colours = 7
p_no_red_ball = comb(60, 20) / comb(70, 20)
p_red_ball = 1 - p_no_red_ball
result = p_red_ball * colours

print(result)
