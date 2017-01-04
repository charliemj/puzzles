"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def string_reverse(string):
    return string[::-1]

def is_equal(string1, string2):
    if string1 == string2:
        return True
    return False

def largest_palindrome_product(num_digits):
    x = "9"*num_digits
    y = "9"*num_digits

    a = int(x)
    b = int(y)

    max_pal = []

    while True:
        prod = str(a*b)

        reversed_string = string_reverse(prod)

        if is_equal(reversed_string,prod):
                max_pal.append(int(prod))

        #decrease a and b
        if b == 1:
            a -= 1

        b -= 1

        if b == 0:
            b = int(y)

        if a == 0:
            return max(max_pal)

print largest_palindrome_product(2)
print largest_palindrome_product(3)
