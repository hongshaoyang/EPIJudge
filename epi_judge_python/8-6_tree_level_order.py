from test_framework import generic_test
from binary_tree_node import BinaryTreeNode

# 8.6 Compute binary tree nodes in order of increasing depth
def binary_tree_depth_order(tree: BinaryTreeNode):
    res = []
    if not tree:
        return res
    
    curr_depth_nodes = [tree]
    while curr_depth_nodes:
        res.append([n.data for n in curr_depth_nodes])
        curr_depth_nodes = [c for n in curr_depth_nodes for c in (n.left, n.right) if c]
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
