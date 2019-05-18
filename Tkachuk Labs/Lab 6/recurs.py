def fast_exp(b, n):
    def even(n):
        if n % 2 == 0:
            return 1
        return 0

    if n == 0:
        return 1
    if even(n):
        return fast_exp(b, n / 2) ** 2
    return b * fast_exp(b, n - 1)
