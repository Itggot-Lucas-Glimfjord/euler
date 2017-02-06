"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def list_primes(nPrimes):
    primes = [3]
    i = 3
    while len(primes) < nPrimes-1:
        foundDivider = 0

        for j in range(len(primes)):
            if i%primes[j] == 0:
                foundDivider = 1
                break

        if not foundDivider:
            primes.append(i)

        i += 2
    return primes

print (list_primes(10001)[-1])