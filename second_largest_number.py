def second_largest_number(array):
    first_largest = float('-inf')
    second_largest = float('inf')
    for i in array:
        if i > first_largest:
            second_largest = first_largest
            first_largest = i
        elif first_largest > i > second_largest:
            second_largest = i
    return second_largest if second_largest!= float('-inf') else -1
array = [1,2,3,90,4,67,89,98,198,197]
second_largest_number_in_the_array = second_largest_number(array)
print(second_largest_number_in_the_array)