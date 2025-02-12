# finding the column sum
m = 3
n = 2
for i in range(m):
    for j in range(n):
        # Add the element
        sum += arr[j][i]

    # Print the column sum
    print("Sum of the column", i, "=", sum)

    # Reset the sum
    sum = 0
