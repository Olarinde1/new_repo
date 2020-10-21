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
print()
print("--------------------------------------------This is another code----------------------------------------------------")
print()


def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum
print(sum_squares(10)) # Should be 285

# use for loops when there is a sequence of elements you want to iterate
# use while loops when you want to repeat an action until a condition changes/a condition is false


product = 1
for n in range(1, 11):
    product *= n

print(product) 

def to_celcuis(x):
    return (x - 32) * 5/9

for x in range(0, 101, 10):
    print(x, to_celcuis(x))

print()
print("--------------------------------------------This is another code----------------------------------------------------")
print()

for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()

teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']

for home_teams in teams:
    for away_teams in teams:
        if home_teams != away_teams:
            print(home_teams + ' vs ' + away_teams)

print()
print("--------------------------------------------This is another code----------------------------------------------------")
print()

def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)

greet_friends(['Taylor', 'Luisa', 'Jamal', 'Eli'])
print()
greet_friends('Alli')
print()
greet_friends(['Alli'])
print()

def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n -1)

print(factorial(9))

def factorial(n):
    print("Factorial called with ", str(n))
    if n < 2: 
        print('Returning 1')
        return 1
    result = n * factorial(n - 1)
    print("Returning " + str(result) + " for factorial of ", str(n))
    return result

factorial(9)

print()
print()

def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return 1

  # Recursive case: keep dividing number by base.
  return is_power_of(number, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False