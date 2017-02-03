"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""
import maths


multiples = multiple3 = multiple5 = []

for i in range(math.floor(1000/3)):
    multiple3.append(i*3)
    
for i in range(math.floor(100/5)):
    multiple5.append(i*5)
    

print( sum(multiple3 + multiple5))