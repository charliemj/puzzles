'''
https://projecteuler.net/problem=1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def mul_3_5(n):
    ans = 0
    for num in range(0, n):
        if num%3 == 0 or num%5 == 0:
            ans += num
    return ans

print mul_3_5(1000)