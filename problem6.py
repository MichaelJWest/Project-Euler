def sum_of_sq(n):
	x=n*(n+1)*(2*n+1)*1/6
	return x
def sq_of_sum(n):
	y=n**2*(n+1)**2*1/4
	return y
	
print sq_of_sum(100) - sum_of_sq(100)

	