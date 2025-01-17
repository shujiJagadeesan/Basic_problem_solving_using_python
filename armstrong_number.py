def is_armstrong_number(given_number):
    number = given_number
    digit_count = 0
    sum=0
    while number > 0:
        digit_count += 1
        number //= 10
    print(digit_count)

    while given_number > 0:
        # digit_count += 1
        digit = given_number % 10
        answer = digit ** digit_count
        sum += answer
        given_number //= 10
    return sum
given_number = 1634
armstrong_number = is_armstrong_number(given_number)
if armstrong_number == given_number:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")

