def to_find_minimum_and_maximum_element_in_an_array(arr):
    arr.sort()
    minmax = {"minimum": arr[0], "maximum": arr[-1]}
    return minmax
arr = [23,45,67,76,78,23]
get_minimum_maximum = to_find_minimum_and_maximum_element_in_an_array(arr)
print("Minimum element is", get_minimum_maximum["minimum"])
print("Maximum element is", get_minimum_maximum["maximum"])
