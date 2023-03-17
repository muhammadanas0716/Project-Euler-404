### Question

# A Pythagorean triplet is a set of three natural numbers, 𝑎 <𝑏< 𝑐, for which,

# 𝑎^2 + 𝑏^2 = 𝑐^2

# For example, 3^+ 4^2 = 9 + 16 = 25 = 5^2
# There exists exactly one Pythagorean triplet for which 𝑎 + 𝑏 + 𝑐= 1000
# Find the product 𝑎.𝑏.𝑐


## Problem Link: https://projecteuler.net/problem=9

### Start Code ###

from math import sqrt

a = 1
b = a + 1
targetNumber = 1000

j = 1
for a in range(1, targetNumber):
    for b in range(a + 1, targetNumber):
        cSquared = pow(a, 2) + pow(b, 2)
        c = sqrt(cSquared)
        
        if (isinstance(c, int) or c.is_integer()) and (sum([a, b, c]) == 1000):
            print("Success")
            print(f"a = {a}; b = {b}; c = {c}")
            print(f"Product: {a * b * c}")

### End Code ###


# OUTPUT: 31875000
