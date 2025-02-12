def two_sum(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement],i]
        seen[num] = i
    return []
arr = [2,11,15,7]
target = 9
two_sum_pair_index = two_sum(arr,target)
print(two_sum_pair_index)