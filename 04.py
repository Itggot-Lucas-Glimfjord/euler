"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

found = 0
for a in xrange(999,100,-1):
    for b in xrange(999,100,-1):
        number = a*b
        if str(number) == str(number)[::-1]:
            print number, a, b
            found = 1
            break
