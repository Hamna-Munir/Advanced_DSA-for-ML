"""
backtracking_permutations.py
Generate all permutations of a list using backtracking.
"""

def permutations(nums, path=[], result=[]):
    if not nums:
        result.append(path)
        return
    for i in range(len(nums)):
        permutations(nums[:i] + nums[i+1:], path + [nums[i]], result)
    return result

if __name__ == "__main__":
    nums = [1, 2, 3]
    result = permutations(nums, [], [])
    print("All permutations of", nums, ":", result)

# Output:
# All permutations of [1, 2, 3] : [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
