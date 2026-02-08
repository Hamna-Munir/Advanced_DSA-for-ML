"""
recursion_fibonacci.py
Compute nth Fibonacci number using recursion.
"""

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    n = 6
    print(f"Fibonacci number at position {n}:", fibonacci(n))

# Output:
# Fibonacci number at position 6: 8
