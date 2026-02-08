"""
recursion_factorial.py
Compute factorial using recursion.
"""

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    num = 5
    print(f"Factorial of {num}:", factorial(num))

# Output:
# Factorial of 5: 120
