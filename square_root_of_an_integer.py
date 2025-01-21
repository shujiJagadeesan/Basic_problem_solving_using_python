def square_root_of_an_integer(number_to_find_its_square_root):
    result = 1
    while result * result <= number_to_find_its_square_root:
        result+=1
#result-1 will be the square root because previously condition is <= so we subtract 1
    return result-1
number = 49
square_root = square_root_of_an_integer(number)
print(square_root)

