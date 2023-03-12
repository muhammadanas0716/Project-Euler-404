#### Problem Statement ####

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?


### Start Code ###

number = 600851475143
largest_prime_factor = None

for i in range(2, int(number ** 0.5 + 1)):
    if number % i == 0:
        # i is a factor, check if it is prime
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            largest_prime_factor = i

print(largest_prime_factor)

### End Code ###

#### OUTPUT: 6857
