#find the biggest and smallest elements of a list
#assumes list of len at least 1
def big_small(A):
    small = A[0]
    big = A[0]
    for num in A:
        if num > big:
            big = num
        if num < small:
            small = num
    return small, big

#A = [9,4,3,22,1,2,6,5,0,11,23]
#print big_small(A)
