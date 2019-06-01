def getValueA(n, m):
    if n != 0 and m != 0:
        return getValueA(n-1,getValueA(n,m-1))
    elif n != 0 and m == 0:
        return getValueA(n-1, 1)
    elif n == 0:
        return m+1
