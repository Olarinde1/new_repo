def print_prime_factors(num):

    factor = 2

    while factor <= num:
        if num % factor == 0:
            print(factor)
            num = num / factor
        else:
            factor += 1

print_prime_factors(1000)
print()
print("--------------------------------------------This is another code----------------------------------------------------")
print()
def sum_divisors(n):
  sum = 0
  c = 1
  # Return the sum of all divisors of n, not including n
  while c < n:
    if n % c == 0 and n != 0:
      sum += c
    else:
      pass
    
    c += 1

  return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114


print()
print("--------------------------------------------This is another code----------------------------------------------------")
print()

def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = multiplier * number 
		# What is the additional condition to exit out of the loop?
		if result > 25:
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier+= 1

multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5) 
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)	
# Should print: 8x1=8 8x2=16 8x3=24