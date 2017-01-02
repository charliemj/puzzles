#based off of this (I don't have their node class so I implemented  using lists)
#https://leetcode.com/problems/add-two-numbers/
'''
You are given two linked lists representing two non-negative numbers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''
#I'm assuming base 10

def addTwoNums(LLa, LLb):
    out = []
    for i in range(0, max(len(LLa),len(LLb))):
        if LLa[i] is None:
            out.append(LLb[i])
        if LLb[i] is None:
            out.append(LLa[i])
        if LLa[i] + LLb[i] <= 9:
            out.append(LLa[i] + LLb[i])
        else:
            ones_place = (LLa[i] + LLb[i])-10
            out.append(ones_place)
            LLa[i+1] += 1
    return out

# a = [2,4,3]
# b = [5,6,4]
# c = [0,0,0]
#print addTwoNums(a,c)