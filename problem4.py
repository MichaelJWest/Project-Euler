#find largest palindromic number that is the product of two 3-digit numbers

		
list1=[]
for i in range(10000, 998001):
	if str(i) == str(i)[::-1]:
		list1.append(i)

list2=[]		
def append_numbers_with_3digit_factors(x):
	for i in range(1, x+1):
		if x%i == 0 and len(str(i)) == 3 and len(str(x/i)) == 3:
			list2.append(x)
		
for i in list1:
	append_numbers_with_3digit_factors(i)

print list2[-1]