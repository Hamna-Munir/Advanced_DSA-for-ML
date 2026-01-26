# Segment Tree for Range Sum Query

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)

        # Build tree
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]

        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, value):
        pos = index + self.n
        self.tree[pos] = value

        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]

    def query(self, left, right):
        result = 0
        left += self.n
        right += self.n

        while left <= right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            if right % 2 == 0:
                result += self.tree[right]
                right -= 1
            left //= 2
            right //= 2

        return result


# Example
arr = [1, 3, 5, 7, 9, 11]
st = SegmentTree(arr)

print("Sum from index 1 to 4:", st.query(1, 4))

st.update(3, 10)
print("After update, sum from index 1 to 4:", st.query(1, 4))

# Output
# Sum from index 1 to 4: 24
# After update, sum from index 1 to 4: 27
