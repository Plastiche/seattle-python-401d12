def check_brackets(txt):
    """
    recursive bracket validator
    """

    braces = {
            ')':'(',
            ']':'[',
            '}':'{',
        }

    stack = Stack()

    def walk(index = 0):
        char = txt[index]

        if char in braces.values(): # openers
            stack.push(char)

        if char in braces: # closers
            candidate = stack.peek()
            if candidate != braces[char]:
                return False
            stack.pop()
            

        if index + 1 < len(txt):
            return walk(index + 1)

        return True


    return walk() and stack.is_empty()

def check_brackets_iterative(txt):
    """
    iterative bracket validator
    """

    braces = {
        ')':'(',
        ']':'[',
        '}':'{',
    }
    
    stack = Stack()

    for char in txt:
        if char in braces.values():
            stack.push(char)
            continue

        if char in braces:
            if stack.peek() != braces[char]:
                return False
            stack.pop()
            

    return stack.is_empty()


# Helper Classes

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)

    def remove(self):
        removed = self.head
        self.head = self.head.next
        return removed

class Stack:
    def __init__(self):
        self.lst = LinkedList()

    def pop(self):
        return self.lst.remove().value

    def push(self, value):
        self.lst.insert(value)

    def peek(self):
        return self.lst.head and self.lst.head.value

    def is_empty(self):
        return self.lst.head is None


class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next



    