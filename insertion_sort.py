arr = [11,10,13,14,5,6]
n = len(arr)
for i in range(1,n):
    key = arr[i]
    j = i-1
    while j>=0 and key<arr[j]:
        arr[j+1] = arr[j]
        j-=1
    arr[j+1] = key
print(arr)
