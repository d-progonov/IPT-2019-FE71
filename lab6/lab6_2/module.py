def getNSum(n, elem, step):
    if n == 1:
        return elem
    else:
        return elem+(n-1)*step+getNSum(n-1, elem, step)