### Question

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


## Problem Link: https://projecteuler.net/problem=10

### Start Code ###

primes = []

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        i = 2
        while i <= int(n ** 0.5) + 1:
            if n % i == 0:
                return False
            i += 1
        return True


for i in range(1, 2_000_001):
    if is_prime(i):
        primes.append(i)

print(f"Sum:  {sum(primes)}")

### End Code ###


# OUTPUT: 142913828922
