#### Problem Statement ####

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

## Problem Link: https://projecteuler.net/problem=4

### Start Code ###
pans = []
for i in range(1, 1000):
    for j in range(1, 1000):
        num = i * j
        num = str(num)
        if num[::-1] == num:
            int(num)
            pans.append(int(num))

print(max(set(pans)))

### End Code ###

#### OUTPUT: 906609
