#### Problem Statement ####


# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.



### Start Code ###

values = [1, 2]
for i in range(1, 50):
    if values[-1:] < [4_000_000]:
        values.append(sum(values[-2:]))

summation = [num for num in values if num % 2 == 0]
print(sum(summation))

summation = [num for num in values]

### End Code ###

#### OUTPUT: 4613732
