"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sum_of_squares(n):
    return reduce(lambda x,y: x+y, map(lambda x: x**2, range(1, n+1)))

def square_the_sum(n):
    return reduce(lambda x,y: x+y, range(1, n+1))**2

def sum_square_difference(n):
    return square_the_sum(n) - sum_of_squares(n) 

print sum_square_difference(10)

print sum_square_difference(100)

