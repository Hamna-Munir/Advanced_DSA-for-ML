"""
sets_example.py
Demonstrates set operations and uniqueness handling.
"""

def set_operations():
    A = {1, 2, 3}
    B = {3, 4, 5}

    print("Set A:", A)
    print("Set B:", B)

    print("Union:", A | B)
    print("Intersection:", A & B)
    print("Difference A-B:", A - B)


def remove_duplicates():
    numbers = [1, 2, 2, 3, 4, 4, 5]
    unique = set(numbers)

    print("Original list:", numbers)
    print("Unique elements:", unique)


if __name__ == "__main__":
    set_operations()
    print()
    remove_duplicates()


# OUTPUT
# Set A: {1, 2, 3}
# Set B: {3, 4, 5}
# Union: {1, 2, 3, 4, 5}
# Intersection: {3}
# Difference A-B: {1, 2}

# Original list: [1, 2, 2, 3, 4, 4, 5]
# Unique elements: {1, 2, 3, 4, 5}
