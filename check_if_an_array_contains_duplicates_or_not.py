def check_if_an_array_contains_duplicates_or_not(nums):
    seen_numbers = set()
    for num in nums:
        if num in seen_numbers:
            return True
        seen_numbers.add(num)
    return False
nums = [1,23,45,6,7,1]
checking_duplicates = check_if_an_array_contains_duplicates_or_not(nums)
if(checking_duplicates):
    print("Yes, the array contains duplicates")
else:
    print("No, the array does not contain any duplicates")

