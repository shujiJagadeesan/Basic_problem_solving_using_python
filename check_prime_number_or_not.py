def check_prime_number_or_not(number):
    if number > 1:
        for i in range(2,(number//2)+1):
            if number % i == 0:
                print(number , "is not a prime number")
                break
        else:
            print("It is a prime number")
    else:
        print("It is not a prime number ")
number = int(input("Enter a number to find whether it is prime or not: "))
check_prime_number_or_not(number)
