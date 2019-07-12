class LinkedList: 
    
    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)

    def __str__(self):
        return 'I am what I am'


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

