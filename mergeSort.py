def merge(A, B):
    result = []
    if A[0] < B[0]:
        result.append(A[0])
        A = A[1:]
    else:  #B[0] <= A[0]
        result.append(B[0])
        B = B[1:]
    if len(A) == 0:
        result.extend(B)
        return result
    elif len(B) == 0:
        result.extend(A)
        return result
    else:
        result.extend(merge(A, B))
        return result


# def merge(A,B):
#     result = []
#     Ai, Bi = 0,0
#     while (Ai < len(A)) and (Bi < len(B)):
#         if A[Ai] <= B[Bi]:
#             result.append(A[Ai])
#             Ai +=1
#         else: #A[Ai] >= B[Bi]
#             result.append(B[Bi])
#             Bi +=1

#     result.extend(B[Bi:])
#     result.extend(A[Ai:])
    
#     return result

# def Mmerge(left, right):
#     result = []
#     left_idx, right_idx = 0, 0
#     while left_idx < len(left) and right_idx < len(right):
#         # change the direction of this comparison to change the direction of the sort
#         if left[left_idx] <= right[right_idx]:
#             result.append(left[left_idx])
#             left_idx += 1
#         else:
#             result.append(right[right_idx])
#             right_idx += 1

#     if left:
#         result.extend(left[left_idx:])
#     if right:
#         result.extend(right[right_idx:])
#     return result

# A = [1,2,7,11,12]
# B = [4,5,6,9,10]
#print merge(A,B)
#print Mmerge(A,B)

def merge_sort(A):
    if len(A) == 1:
        return A
    
    mid = len(A)/2
    left = A[:mid]
    right = A[mid:]
    a = merge_sort(left)
    b = merge_sort(right)

    return merge(a,b) 

#C = [4,52,3,5,6,7,5,4,3,2]
#print merge_sort(C)

def kthLargest(A,k):
    sortedList = merge_sort(A)[::-1]
    return sortedList[k-1]
#print kthLargest(C,1)

