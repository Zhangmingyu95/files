__author__ = 'mingyu.zhang'

class BTree:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None

class test_BTree:
    def test_create(self):
        tree=BTree(0)
        tree.left=BTree(1)
        tree.right=BTree(2)
        tree.left.left=BTree(3)
        tree.left.right=BTree(4)
        tree.right.left=BTree(5)
        tree.right.right=BTree(6)
        tree.right.right.right=BTree(7)