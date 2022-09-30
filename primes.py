"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes<1:
    	raise ValueError("number of primes must be greater than 0")
    list = []
    count =0
    current_num = 2
    isPrime = True
    while count<number_of_primes:
    	for i in range(2,current_num):
    		if current_num%i ==0:
    			isPrime = False
    			break
    	if isPrime:
    		list.append(current_num)
    		count+=1
    	current_num += 1
    	isPrime = True
    return list
