from binary_tree_node import BinaryTreeNode 
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder, inorder):
    if not inorder:
        return None

    tree = BinaryTreeNode(preorder[0])
    x = inorder.index(preorder[0])
    left, right = inorder[:x], inorder[x+1:]
    if left:
        tree.left = binary_tree_from_preorder_inorder(preorder[1:len(left)+1], left)
    if right:
        tree.right = binary_tree_from_preorder_inorder(preorder[len(left)+1:], right)
    return tree

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
