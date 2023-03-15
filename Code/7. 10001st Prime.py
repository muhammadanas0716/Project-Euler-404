### Question

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?


### Start Code ###
def is_prime(n):
    if n < 2:  # Numbers less than 2 are not prime
        return False
    for i in range(2, int(n**0.5) + 1):  # Check for factors up to the square root of n
        if n % i == 0:  # If n is divisible by i, it is not prime
            return False
        return True


count = 0  # Initialize a counter for prime numbers
num = 2  # Start with the first prime number

while count < 10001:  # Keep checking until we find the 10001th prime
    if is_prime(num):  # If num is prime, increment the counter
        count += 1
    if count == 10001:  # If we have found the 10001th prime, print it and break out of the loop
        print("The 10001th prime number is:", num)
        break
    num += 1  # Increment the number to check for the next prime
### End Code ###


# OUTPUT: 104743