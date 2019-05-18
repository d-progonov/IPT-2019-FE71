def prime_check(n):
    numbers = list(range(2, n + 1))
    for i in numbers:
        if i != 0:
            for k in range(2 * i, n + 1, i):
                numbers[k - 2] = 0

    primes = [x for x in numbers if x != 0]

    final = []

    for position in range(len(primes)):
        z = n - primes[position]
        if z in primes:
            final.append("The pair of these elements from prime number list give our value in sum:")
            final.append(z)
            final.append("+")
            final.append(primes[position])
            final.append('\n')
        position += 1

    str1 = ''.join(str(e) for e in final)

    return (str1)
