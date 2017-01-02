def findMax(A):
    if len(A) == 1:
        return A[0]
    else:
        thing = findMax(A[1:])
        if thing > A[0]:
            return thing
        else:
            return A[0]
# a = [0,4,2,11,3,4,3,2,678,87,6,5,3,433]
# print findMax(a)