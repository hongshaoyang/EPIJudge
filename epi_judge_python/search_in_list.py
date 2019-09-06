from test_framework import generic_test
from list_node import ListNode

def search_list(L: ListNode, key: int):
    while L:
        if L.data == key:
            return L
        L = L.next
    return L


def search_list_wrapper(L, key):
    result = search_list(L, key)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_in_list.py", 'search_in_list.tsv', search_list_wrapper))
