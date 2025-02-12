arr=[10,20,20,10,30,40,50,40,0]
arr1=[]
arr2=[]
for i in range(len(arr)):
    if arr[i] not in arr1:
        arr1.append(arr[i])
    elif arr[i] in arr1:
        arr2.append(arr[i])
sum = 0
for i in range(len(arr1)):
    if arr1[i] not in arr2:
        sum+=arr1[i]
print(sum, end=" ")