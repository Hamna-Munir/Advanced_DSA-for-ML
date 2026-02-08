"""
backtracking_subsets.py
Generate all subsets of a list using backtracking.
"""

def subsets(nums, index=0, path=[], result=[]):
    result.append(path)
    for i in range(index, len(nums)):
        subsets(nums, i+1, path + [nums[i]], result)
    return result

if __name__ == "__main__":
    nums = [1, 2, 3]
    result = subsets(nums)
    print("All subsets of", nums, ":", result)

# Output:
# All subsets of [1, 2, 3] : [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
