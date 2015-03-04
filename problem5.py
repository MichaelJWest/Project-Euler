#2520 is the smallest number that can be divided by each of the numbers from 1 to 
#10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers 
#from 1 to 20?

def gcd(a, b): 
	return b and gcd(b, a % b) or a
def lcm(a, b): 
	return a * b / gcd(a, b)

multiple = 20
for i in xrange(10, 21):
    multiple = lcm(multiple, i)

print multiple