import math

def progress(a0, step, n):
    if n == 1:
        return a0
    elif a0 == float('inf') or step == float('inf'):
        return str("The sum of your progression is Infinity")
    else:
        return a0 + (n - 1) * step + progress(a0, step, n - 1)