# Divide and Conquer Example
# Sum of Array

def divide_sum(arr):

    if len(arr) == 1:
        return arr[0]

    mid = len(arr) // 2

    left_sum = divide_sum(arr[:mid])
    right_sum = divide_sum(arr[mid:])

    return left_sum + right_sum


numbers = [1, 2, 3, 4, 5]

print("Sum:", divide_sum(numbers))


# Output
# Sum: 15
