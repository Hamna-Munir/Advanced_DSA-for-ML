# Doubly Linked List Examples

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("NULL")


# Example usage
dll = DoublyLinkedList()
dll.insert_at_head(3)
dll.insert_at_head(2)
dll.insert_at_head(1)
dll.traverse_forward()

# Output:
# 1 <-> 2 <-> 3 <-> NULL
