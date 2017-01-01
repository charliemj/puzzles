def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

#print fact(6)

def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else: 
        return fib(n-1)+fib(n-2)

# for i in range(8):
#     print fib(i)


def flatten(seq):
    res = []
    if not isinstance(seq, list):
        res.append(seq)
    else: #still a list of lists
        if len(seq) == 0:
            return []
        else: 
            return flatten(seq[0]) + flatten(seq[1:])  
    return res

#A = [[1, 2, 3], [[[1]]], 6, [2, 3, [12, 9, 8, 6], 47], [1, []]]
#print flatten(A)

def perm(s):
    res =[]
    if len(s) == 1:
        res.append(s)
        return res
    for el in range(len(s)):
        a = s[:el]+[el:]
        res.extend([])



