from test_framework import generic_test
from list_node import ListNode

# 7.1 Merge 2 sorted lists
def merge_two_sorted_lists(L1: ListNode, L2: ListNode) -> ListNode:
    dummy = tail = ListNode()
    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    # append to rest of LL
    tail.next = L1 if L1 else L2
    return dummy.next



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
