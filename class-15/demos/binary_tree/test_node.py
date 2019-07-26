from binary_tree import Node

def test_exists():
    assert Node

def test_has_value():
    n = Node('apple')
    assert n.value == 'apple'
    assert n.left == None
    assert n.right == None