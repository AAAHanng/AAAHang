# Coding  :utf-8
# Time   :2023/3/4 
# File   :BreathFirstSearch.py
# Author  : AAAHang

class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add_element(self, node_value):
        node = Node(node_value)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]

        while True:
            pop_node = queue.pop(0)

            if pop_node.left is None:
                pop_node.left = node
                return
            else:
                queue.append(pop_node.left)

            if pop_node.right is None:
                pop_node.right = node
                return
            else:
                queue.append(pop_node.right)

    def BFS(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            pop_node = queue.pop(0)
            print(pop_node.val, end=" ")
            if pop_node.left is not None:
                queue.append(pop_node.left)
            if pop_node.right is not None:
                queue.append(pop_node.right)


if __name__ == '__main__':
    tree = Tree()
    tree.add_element(1)
    tree.add_element(2)
    tree.add_element(3)
    tree.add_element(4)
    tree.add_element(5)
    tree.add_element(6)
    tree.BFS()

