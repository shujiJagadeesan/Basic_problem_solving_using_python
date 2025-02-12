def sort_an_array(arr):
    sorted_list = []
    for num in arr:
        inserted = False
        n = len(sorted_list)
        for i in range(n):
            if num < sorted_list[i]:
                sorted_list.insert(i,num)
                inserted = True
                break
        if not inserted:
            sorted_list.append(num)
    return sorted_list
arr = [12,3,23,4,7,2,1,0,8]
result = sort_an_array(arr)
print(result)