
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)
     

class Quez():
    """
    WARNING: This code might be WRONG!!!!
    WARNING: Use at own risk
    WARNING: On the other hand it might be right ;)
    """


    def __init__(self):
        self._lst = LinkedList()

    def peek(self):
        return self._lst.head and self._lst.head.value

    def enqueue(self, value):
        self._lst.insert(value)

    def dequeue(self):
        pass


class Stack:
    """
    Public attributes:
    pop() -> *
    push(value) -> None
    peek() -> *
    """

    def __init__(self):
        self._lst = LinkedList()

    def pop(self):
        pass

    def push(self, value):
        self._lst.insert(value)

    def peek(self):
        return self._lst.head and self._lst.head.value