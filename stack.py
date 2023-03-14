class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None

    def push(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    def pop(self):
        if not self.is_empty():
            node = self.head
            self.head = node.next
            return node.data

    def peek(self):
        if not self.is_empty():
            return self.head.data

    def is_empty(self):
        return self.head is None
