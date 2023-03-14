class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            current = self.root
            while True:
                if item < current.data:
                    if current.left is None:
                        current.left = node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = node
                        break
                    else:
                        current = current.right
        self.size += 1

    def delete(self, item):
        self.root = self._delete(self.root, item)

    def _delete(self, node, item):
        if node is None:
            return None
        if item < node.data:
            node.left = self._delete(node.left, item)
        elif item > node.data:
            node.right = self._delete(node.right, item)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_node = self._find_min(node.right)
                node.data = min_node.data
                node.right = self._delete(node.right, min_node.data)
        self.size -= 1
        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def search(self, item):
        current = self.root
        while current is not None:
            if item == current.data:
                return True
            elif item < current.data:
                current = current.left
            else:
                current = current.right
        return False

    def size(self):
        return self.size
