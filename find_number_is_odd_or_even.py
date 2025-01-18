def to_find_number_is_odd_or_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
number = 21
number_is_odd_or_even = to_find_number_is_odd_or_even(number)
if number_is_odd_or_even:
    print(number, " is even")
else:
    print(number, " is odd")