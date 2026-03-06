# Binary Search Example

def binary_search(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


data = [2, 4, 6, 8, 10, 12, 14]

target = 10

print("Array:", data)
print("Target:", target)

result = binary_search(data, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")


# Output
# Array: [2, 4, 6, 8, 10, 12, 14]
# Target: 10
# Element found at index: 4
