""""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def smallest_multiple(num_range):
    ans = 1
    found = False
    i=0
    memo = {0:0}
    while not found:
        i+=1
        for num in range(1,num_range+1): #check if the number is divisible by each num in the range        
            if ans%num != 0: #does not divide
                ans += memo[num-1] + num*i
                break
            elif ans%num == 0:
                memo[num] = ans

            if num == num_range:
                found = True
                result = ans
        #print i
    return "answer= ", result

print smallest_multiple(10)
# print smallest_multiple(11)
# print smallest_multiple(12)
# print smallest_multiple(13)

#once we have the answer for a smaller number in the range, find the next num in range by doing num*i and inc i til works, 