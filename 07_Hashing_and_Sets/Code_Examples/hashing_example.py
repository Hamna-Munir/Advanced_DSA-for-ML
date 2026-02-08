"""
hashing_example.py
Demonstrates how hashing enables fast lookup.
"""

def hashing_demo():
    # Simulating hashing with Python set
    data = [10, 20, 30, 20, 10]

    hashed_storage = set(data)

    print("Original data:", data)
    print("After hashing (duplicates removed):", hashed_storage)

    # Fast membership lookup
    value = 30
    print(f"Is {value} present?", value in hashed_storage)


if __name__ == "__main__":
    hashing_demo()

# OUTPUT 
# Original data: [10, 20, 30, 20, 10]
# After hashing (duplicates removed): {10, 20, 30}
# Is 30 present? True
