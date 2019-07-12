from camels import LinkedList, Node

def test_exists():
    assert LinkedList

def test_creation():
    ll = LinkedList()
    assert ll

def test_head_is_none():
    ll = LinkedList()
    assert ll.head is None

def test_add_to_empty():
    ll = LinkedList()
    ll.insert('apple')
    assert ll.head.value == 'apple'

def test_add_again_to_empty():
    ll = LinkedList()
    ll.insert('banana')
    assert ll.head.value == 'banana'

def test_add_to_empty_check_next():
    ll = LinkedList()
    ll.insert('apple')
    assert ll.head.next is None

def test_insert_falafel_to_cucumber():
    ll = LinkedList()
    ll.insert('cucumber')
    ll.insert('falafel')
    assert ll.head.value == 'falafel'
    assert ll.head.next.value == 'cucumber' 

def test_insert_falafel_to_cucumber():
    ll = LinkedList()
    ll.insert('cucumber')
    ll.insert('falafel')
    ll.insert('dates')
    assert ll.head.value == 'dates'
    assert ll.head.next.value == 'falafel'
    assert ll.head.next.next.value == 'cucumber'
    assert ll.head.next.next.next is None

# def test_str():
#     ll = LinkedList()
#     assert str(ll) == 'whatever'

def test_node():

    apple = Node('apple')
    banana = Node('banana', apple)
    assert banana.next.value == 'apple'

    cucumber = Node('cucumber', next=banana)
    assert cucumber.next.value == 'banana'


