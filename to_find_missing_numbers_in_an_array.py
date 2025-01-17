def to_find_missing_numbers_in_an_array(array):
    n = len(array) + 1
    expected_sum_to_find_missing_number_till_n =(n*(n+1)) // 2
    total_sum_of_elements_in_array = sum(array)
    missing_number = expected_sum_to_find_missing_number_till_n - total_sum_of_elements_in_array
    return  missing_number
array = [1,2,3,4,5]
result = to_find_missing_numbers_in_an_array(array)
print(result)