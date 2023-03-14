class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        node = Node(item)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if not self.is_empty():
            node = self.front
            self.front = node.next
            if self.front is None:
                self.rear = None
            return node.data

    def peek(self):
        if not self.is_empty():
            return self.front.data

    def is_empty(self):
        return self.front is None
