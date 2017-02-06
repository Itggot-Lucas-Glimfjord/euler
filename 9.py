"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

end = 0
for a in xrange(1,1001):
    for b in xrange(1,1001-a):
        for c in xrange(1,1001-b):
            if a + b + c == 1000 and a**2 + b**2 == c**2:
                print(a*b*c)
                end = 1
                break
        if end:
            break
    if end:
        break

