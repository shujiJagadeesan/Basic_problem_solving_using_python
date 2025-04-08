def check_perfect_number_or_not(number):
    sum_of_divisors_of_the_number = 0
    for i in range(1,number):
        if number % i == 0:
            sum_of_divisors_of_the_number = sum_of_divisors_of_the_number + i
    return True if sum_of_divisors_of_the_number == number else False
number = 1
is_perfect_number = check_perfect_number_or_not(number)
if (is_perfect_number):
    print("It is a perfect number")
else:
    print("It is not a perfect number")


