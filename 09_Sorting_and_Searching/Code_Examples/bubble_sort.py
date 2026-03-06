# Bubble Sort Example

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


data = [64, 34, 25, 12, 22, 11, 90]

print("Original Array:", data)

sorted_array = bubble_sort(data)

print("Sorted Array:", sorted_array)


# Output
# Original Array: [64, 34, 25, 12, 22, 11, 90]
# Sorted Array: [11, 12, 22, 25, 34, 64, 90]
