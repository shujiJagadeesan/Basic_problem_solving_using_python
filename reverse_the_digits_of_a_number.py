def reverse_the_digits_of_a_number(number):
    reverse = 0
    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number //= 10
    return reverse
number = int(input("Enter a number to reverse it: "))
reversed_number = reverse_the_digits_of_a_number(number)
print(reversed_number,"is the reversed version of", number)