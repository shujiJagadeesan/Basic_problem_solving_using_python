def find_factorial(number):
    factorial = 1
    i = 1
    while i <= number:
        factorial = factorial * i
        i += 1
    return factorial
number = 2
factorial_of_the_number = find_factorial(number)
print(factorial_of_the_number)