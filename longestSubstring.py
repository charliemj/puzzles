#https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

def longSubStr(string):
    seenChars = set()
    substring = ''
    for char in string:
        if char not in seenChars:
            substring = substring+char
            seenChars.add(char)
        else: #it has been seen and is therefore a repeat
            return substring
    return substring

# string = "bbbbb"
# print longSubStr(string)
