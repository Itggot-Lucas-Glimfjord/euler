"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math
number = 600851475143

def list_primes(nmax):
    primes = [2]

    for i in xrange(3,nmax,2):
        foundDivider = 0

        for j in range(len(primes)):
            if i%primes[j] == 0:
                foundDivider = 1
                break

        if not foundDivider:
            primes.append(i)
    return primes

primes = list_primes(int(number**0.5))

for prime in primes[::-1]:
    if number%prime == 0:
        print(prime)
        break
