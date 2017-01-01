def coins(value, denoms):
    memo = {}

    def change(value):
        if value in memo:
            return memo[value]
        if value == 0:
            return 0
        if value < 0:
            return float("inf")

        memo[value] = min([1+change(value-denom) for denom in denoms]) 
        return memo[value]
    return change(value)

v = 20
d = [2,5,4]
print coins(v,d)