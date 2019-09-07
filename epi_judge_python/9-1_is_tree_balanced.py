from test_framework import generic_test
from binary_tree_node import BinaryTreeNode
from collections import namedtuple

# 9.1 test if a binary tree is height-balanced
Balanced = namedtuple("Balanced", ["balanced", "height"])

def is_balanced_binary_tree(tree: BinaryTreeNode):
    return inner(tree).balanced

def inner(tree: BinaryTreeNode):
    if not tree:
        return Balanced(True, -1)
    if not tree.left and not tree.right:
        # base case: a leaf is balanced with height 0
        return Balanced(True, 0)
    
    left = inner(tree.left)
    if not left.balanced:
        return Balanced(False, 0)
    right = inner(tree.right)
    if not right.balanced:
        return Balanced(False, 0)

    balanced = abs(left.height - right.height) <= 1
    curr_height = max(left.height, right.height) + 1
    return Balanced(balanced, curr_height)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
