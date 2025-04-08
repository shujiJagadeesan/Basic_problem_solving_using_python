arr = [11, 5, 7, 9, 8]
start = 6
end = 7
total = 0
i = 0
ignore = False  # This flag controls whether to ignore elements

while i < len(arr):
    if arr[i] == start:
        ignore = True  # Start ignoring numbers
        i += 1
        continue  # Skip adding 6 itself

    if arr[i] == end and ignore:
        ignore = False  # Stop ignoring numbers
        i += 1
        continue  # Skip adding 7 itself

    if not ignore:
        total += arr[i]  # Only add if we are not ignoring

    i += 1  # Move to the next element

# If `6` appeared but no `7` was found after it, add `6` back
if start in arr and end not in arr[arr.index(start):]:
    total += start

print(total)
