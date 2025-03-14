def matching_elements_in_an_array(arr):
    seen = set()
    duplicates = set()
    for i in arr:
        if i in seen:
            duplicates.add(i)
        seen.add(i)
    return list(duplicates)
arr = [1,2,4,2,1,5,9,6,5]
matching_elements = matching_elements_in_an_array(arr)
print(matching_elements)