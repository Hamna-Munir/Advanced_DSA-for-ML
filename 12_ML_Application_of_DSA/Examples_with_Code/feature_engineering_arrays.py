# Feature Engineering using Arrays
# Example: Creating feature vectors

import numpy as np

# Dataset: [study_hours, attendance]
data = np.array([
    [5, 1],
    [4, 1],
    [3, 1],
    [2, 0],
    [1, 0]
])

print("Feature Matrix:")
print(data)

# Normalize features
normalized = data / np.max(data, axis=0)

print("\nNormalized Features:")
print(normalized)


# Output
# Feature Matrix:
# [[5 1]
#  [4 1]
#  [3 1]
#  [2 0]
#  [1 0]]
#
# Normalized Features:
# [[1.  1. ]
#  [0.8 1. ]
#  [0.6 1. ]
#  [0.4 0. ]
#  [0.2 0. ]]
