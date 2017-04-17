def longest_substring(string):
    start = 0
    end = len(string)

    result = ""
    for start in range(len(string)):
        for end in range(start+1,len(string)+1):
            a = set(string[start:end+1])
            if len(a) == 2 or len(a) ==1:
                cand = string[start:end+1]
                if len(cand) > len(result):
                    result = cand
    return result

print(longest_substring("ababababbabbbbbbakjfdjkjkbabablkjdfjlk"))
    


