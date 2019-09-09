import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from binary_tree_with_parent_prototype import BinaryTreeNode


# 9.4 Compute the LCA when nodes have parent pointers
def lca(node0: BinaryTreeNode, node1: BinaryTreeNode):
    n0_path, n1_path = [], []
    curr = node0
    while curr:
        n0_path.append(curr)
        curr = curr.parent
    curr = node1
    while curr:
        n1_path.append(curr)
        curr = curr.parent

    n0_path.reverse()
    n1_path.reverse()

    i = 0
    while i < min(len(n0_path), len(n1_path)) and n0_path[i] is n1_path[i]:
        i +=1 
    return n0_path[i-1]




@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor_with_parent.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
