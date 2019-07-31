from binary_tree import BinaryTree, Node, breadth_first_search

def test_exists():
    assert breadth_first_search

def test_prints(capsys):
    tree = BinaryTree()
    apples = Node('apples')
    bananas = Node('bananas')
    cucumbers = Node('cucumbers')
    tree.root = apples
    apples.left = bananas
    apples.right = cucumbers

    breadth_first_search(tree)

    out = capsys.readouterr()
    assert out.out == 'apples\nbananas\ncucumbers\n'

def do_thing(val):
    print(val)

def test_action(capsys):
    tree = BinaryTree()
    apples = Node('apples')
    bananas = Node('bananas')
    cucumbers = Node('cucumbers')
    tree.root = apples
    apples.left = bananas
    apples.right = cucumbers

    lst = []


    breadth_first_search(tree, lambda val: lst.append(val))

    assert lst == ['apples','bananas','cucumbers']