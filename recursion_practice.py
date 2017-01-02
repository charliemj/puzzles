def maxi(A):
    if len(A) == 1:
        return A[0]
    return max(A[0], maxi(A[1:]))

#print maxi([1,3,200,44,1])

def find(A, val):
    if len(A) == 0:
        return False
        
    if A[0] == val:
        return True

    return find(A[1:],val)

# a = [1,3,200,44,1]
# print find(a, 22)

def flatten(A):
    if not isinstance(A, list):
        return [A]
    if len(A) ==0:
        return []
    #A is a list
    return flatten(A[0]) + flatten(A[1:])

def flat(A):
    if not isinstance(A, list):
        return [A]

    return sum([flatten(x) for x in A], [])

a = [[1, 3], [[200]], 44, 1]
# print flatten(a)
# print flat(a)


def findNest(A, val):
    if not isinstance(A, list):
        if A == val:
            return True
        else:
            return False
    #this is a list

    for el in A:
        if findNest(el,val):
            return True
    return False

#print findNest(a,2)




