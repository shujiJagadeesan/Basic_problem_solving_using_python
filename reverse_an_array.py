def reverse_an_array(arr):
    start = 0
    end = len(arr)-1
    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
    return arr
arr = [5,4,3,2,1,0]
reversed_array = reverse_an_array(arr)
print(reversed_array)