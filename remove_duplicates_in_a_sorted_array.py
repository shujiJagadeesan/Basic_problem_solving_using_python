def remove_duplicates_in_a_sorted_array(arr):
    i = 0
    n = len(arr)
    for j in range(n):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return i+1

arr = [0,0,1,1,1,2,2,3,3,4]
length = remove_duplicates_in_a_sorted_array(arr)
print(arr[:length])