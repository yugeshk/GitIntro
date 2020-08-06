def factorial(number_for_factorial):
	# Add code here
	# new comment vikaskok
	if (number_for_factorial == 0):
                ans = 1
        else:
                ans = number_for_factorial*factorial(number_for_factorial-1)
	return ans #Factorial number


def gcd(number_1, number_2):
    # Add code here
    if number_1 > number_2:
            var = number_2
    elif number_2 > number_1:
            var = number_1


    for i in range(1, var+1):
            if((number_1 % i == 0) and (number_2 % i == 0)):
                    ans = i
    return ans #gcd value


def is_palindrome(string_to_check):
	# Add code here
	reverse_string = string_to_check[ : : -1]
	if (string_to_check == reverse_string):
                ans = True
        else:
                ans = False
	return ans #boolean response


#Take input for fib in variable a

print(fib(a))


#Take input for is_prime in variable b, c

print(gcd(b, c))


#Take input for is_palindrome in variable d

print(is_palindrome(d))
