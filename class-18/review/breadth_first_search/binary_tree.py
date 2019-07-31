from collections import deque


class BinaryTree:
    def __init__(self):
        self.root = None


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.append(value)

    def dequeue(self):
        return self.dq.popleft()

    def is_empty(self):
        return len(self.dq) == 0


def breadth_first_search(tree, action=print):

    q = Queue()

    if tree.root:
        q.enqueue(tree.root)

    while not q.is_empty():

        node = q.dequeue()

        if node.left:
            q.enqueue(node.left)

        if node.right:
            q.enqueue(node.right)

        action(node.value)
