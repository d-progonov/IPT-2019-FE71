def task(n):
    numbers = list(range(2, 2 * n + 1))
    for i in numbers:
        if i != 0:
            for k in range(2 * i, 2 * n + 1, i):
                numbers[k - 2] = 0

    primes = [x for x in numbers if x != 0]
    taken = list(filter(lambda x: 2 * n > x > n, primes))
    # print("Prime numbers list:", primes, '\n')
    # print("The range of searching of twin numbers:", taken, '\n')

    result = []

    for i in range(len(taken) - 1):
        if taken[i] == taken[i + 1] - 2:
            result.append("The pairs of these elements are twins:")
            result.append(taken[i])
            result.append(' ')
            result.append("and")
            result.append(' ')
            result.append(taken[i + 1])
            result.append('\n')

    res = ''.join(str(e) for e in result)

    return (res)
