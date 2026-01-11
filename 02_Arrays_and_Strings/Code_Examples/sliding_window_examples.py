# Sliding Window Example
# Maximum sum of subarray of size k

def max_subarray_sum(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i]
        window_sum -= arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


numbers = [2, 1, 5, 1, 3, 2]
print(max_subarray_sum(numbers, 3))

# Output:
# 9
