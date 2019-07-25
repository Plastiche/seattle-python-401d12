def emmm(names, k):
    """
    eeney meeney miney moe
    """

    q = Queue(names)
    
    tiger = None

    while q:
        for i in range(1, k+1):
            tiger = q.dequeue()
            if i != k:
                q.enqueue(tiger)

    return tiger












# helper class

from collections import deque

class Queue:
    """
    Queue class that composes Deque
    """

    def __init__(self, values=None):
        self.dq = deque(values)

    def enqueue(self, value):
        return self.dq.append(value)

    def dequeue(self):
        return self.dq.popleft()

    def __len__(self):
        return len(self.dq)