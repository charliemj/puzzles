def coinsChange(V,v):
    memo = {}
    def Change(V):
            if V in memo:
                    return memo[V]
            if V == 0:
                    return 0
            if V < 0:
                    return float("inf")
            memo[V] = min([1+Change(V-vi) for vi in v])
            return memo[V]
    return Change(V)

V = 800
v = [1,5,10,20]
print coinsChange(V,v)