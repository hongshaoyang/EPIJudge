from test_framework import generic_test
from list_node import ListNode

# 7.2 reverse a sublist
def reverse_sublist(L: ListNode, start: int, finish: int):
    dummy = head = ListNode(0, L)
    for _ in range(1, start):
        head = head.next
    
    curr = head.next
    for _ in range(finish-start):
        temp = curr.next
        # all 3 are moving .next pointers!
        head.next, curr.next, temp.next = temp, temp.next, head.next

    # at the end of the loop, curr becomes the end of the reversed sublist
    return dummy.next   


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
