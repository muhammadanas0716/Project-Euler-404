### Question

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?


### Start Code ###
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True


count = 0
num = 2

while count < 10001:
    if is_prime(num):
        count += 1
    if count == 10001:
        print("The 10001th prime number is:", num)
        break
    num += 1
### End Code ###


# OUTPUT: 104743
