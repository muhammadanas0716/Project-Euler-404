### Project Euler - Question 6:

# Link: `https://projecteuler.net/problem=6`

# The sum of the squares of the first ten natural numbers is:
# $1^2 + 2^2 + ... + 10^2 = 385$

# The square of the sum of the first ten natural numbers is:
# (1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

## Problem Link: https://projecteuler.net/problem=6

### Start Code ###

# Sum of sqaures
sum_of_squares = []
for i in range(1, 101):
    sum_of_squares.append(pow(i, 2)) # Same as `sum_of_squares.append(i ** 2)`

sum_of_squares = sum(sum_of_squares)
print(sum_of_squares)

# Sqaure of Sums
sqaure_of_sums = []
for i in range(1, 101):
    sqaure_of_sums.append(i)

sqaure_of_sums = pow(sum(sqaure_of_sums), 2)
print(sqaure_of_sums)

# Get difference
difference = sqaure_of_sums - sum_of_squares
print(difference)
### End Code ###

#### OUTPUT: 25164150