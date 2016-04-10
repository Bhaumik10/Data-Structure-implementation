class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# Code for pre-order traversal

def preOrderTraverse(subtree):
    if subtree is not None:
        print subtree.data
        preOrderTraverse(subtree.left)
        preOrderTraverse(subtree.right)


# Code for InOrder Traversal

def InorderTraversal(subtree):
    if subtree is not None:
        InorderTraversal(subtree.left)
        print subtree.data
        InorderTraversal(subtree.right)

# Code for PostOrder Traversal

def PostOrderTraverse(subtree):
    if subtree is not None:
        PostOrderTraverse(subtree.left)
        PostOrderTraverse(subtree.right)
        print subtree.data

