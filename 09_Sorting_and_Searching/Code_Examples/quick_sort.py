# Quick Sort Example

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = []
    right = []

    for num in arr[:-1]:

        if num < pivot:
            left.append(num)

        else:
            right.append(num)

    return quick_sort(left) + [pivot] + quick_sort(right)


data = [10, 7, 8, 9, 1, 5]

print("Original Array:", data)

sorted_array = quick_sort(data)

print("Sorted Array:", sorted_array)


# Output
# Original Array: [10, 7, 8, 9, 1, 5]
# Sorted Array: [1, 5, 7, 8, 9, 10]
