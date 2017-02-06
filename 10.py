"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def primes_to(max):
    numbers = [None]*(max+1)
    primes = []
    index = 2

    while index < max+1:

        if numbers[index] == None:

            multiplied_index = index*2
            while multiplied_index < max+1:
                numbers[multiplied_index] = 1
                multiplied_index += index
        index += 1

    for index, num in enumerate(numbers):
        if num != 1:
            primes.append(index)

    return primes

sum = 0
for num in primes_to(2000000)[2::]:
    if num > 1:
        sum += num

print(primes_to(200)[2::])
print (sum)