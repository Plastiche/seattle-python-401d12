class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def in_order(self):

        results = []

        def visit(node):

            # visit left
            if node.left:
                visit(node.left)

            # do the thing
            results.append(node.value)

            # visit right
            if node.right:
                visit(node.right)


        visit(self.root)

        return results

    def pre_order(self):

        results = []

        def visit(node):

            # do the thing
            results.append(node.value)

            # visit left
            if node.left:
                visit(node.left)

            # visit right
            if node.right:
                visit(node.right)


        visit(self.root)

        return results

    def post_order(self):

        results = []

        def visit(node):

            # visit left
            if node.left:
                visit(node.left)

            # visit right
            if node.right:
                visit(node.right)

            # do the thing
            results.append(node.value)



        visit(self.root)

        return results

class BinarySearchTree:
    pass