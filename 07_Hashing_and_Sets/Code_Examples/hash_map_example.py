"""
hash_map_example.py
Demonstrates dictionary (hash map) usage.
"""

def frequency_counter():
    text = "machinelearning"
    freq = {}

    for char in text:
        freq[char] = freq.get(char, 0) + 1

    print("Character frequency:")
    for k, v in freq.items():
        print(k, "->", v)


def lookup_demo():
    student_marks = {
        "Ali": 85,
        "Sara": 92,
        "John": 78
    }

    name = "Sara"
    print(f"{name}'s marks:", student_marks.get(name))


if __name__ == "__main__":
    frequency_counter()
    print()
    lookup_demo()

# OUTPUT
# Character frequency:
# m -> 1
# a -> 2
# c -> 1
# h -> 1
# i -> 1
# n -> 3
# e -> 2
# l -> 1
# r -> 1
# g -> 1

# Sara's marks: 92
