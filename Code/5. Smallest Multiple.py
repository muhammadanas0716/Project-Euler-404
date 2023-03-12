#### Problem Statement ####

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?



### Start Code ###

from math import lcm

# Generate a list of numbers from 1 to 20
numbers = [i for i in range(1, 21)]

# Compute the LCM of the list of numbers using math.lcm
result = lcm(*numbers)
print(result)


# LCM function from maths lib is only available for Python v3.9+
### End Code ###

#### OUTPUT: 232792560
