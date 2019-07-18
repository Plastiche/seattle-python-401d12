from q import Quez, Stack


def test_peek_empty():
    q = Quez()

    assert q.peek() is None

def test_peek_populated():
    q = Quez()

    q.enqueue('apples')
    
    assert q.peek() == 'apples'

def test_dequeue_populated():
    q = Quez()

    q.enqueue('apples')
    
    assert q.peek() == 'apples'

def test_stack_push():
    s = Stack()

    assert s.push('apples') == None

def test_stack_peek_populated():
    s = Stack()

    s.push('apples')

    assert s.peek() == 'apples'



    