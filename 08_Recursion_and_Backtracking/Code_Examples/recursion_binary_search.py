"""
recursion_binary_search.py
Binary search using recursion.
"""

def binary_search(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid-1)
    else:
        return binary_search(arr, target, mid+1, right)

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9]
    target = 7
    index = binary_search(arr, target, 0, len(arr)-1)
    print(f"Element {target} found at index:", index)

# Output:
# Element 7 found at index: 3
