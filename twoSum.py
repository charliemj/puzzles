#https://leetcode.com/problems/two-sum/

#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution.
def twoSum(aList, target):
    for i in range(0, len(aList)):
        for j in range(i+1, len(aList)):
            if i != j:
                if aList[i] + aList[j] == target:
                    return [i, j]

#print twoSum([2, 7, 11, 15],18)
