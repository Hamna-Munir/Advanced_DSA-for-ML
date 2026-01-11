# Circular Linked List Examples

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def traverse(self):
        if not self.head:
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(Back to Head)")


# Example usage
cll = CircularLinkedList()
cll.insert(1)
cll.insert(2)
cll.insert(3)
cll.traverse()

# Output:
# 1 -> 2 -> 3 -> (Back to Head)
