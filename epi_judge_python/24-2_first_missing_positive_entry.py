from test_framework import generic_test


def find_first_missing_positive(A):
    n = len(A)
    for i in range(len(A)):
        k = A[i]
        while (1 <= k <= n) and (A[k-1] != A[i]):
            A[k-1], A[i] = k, A[k-1]
            k = A[i]
    for i in range(len(A)):
        if A[i] != (i+1):
            return i+1
    return n+1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("first_missing_positive_entry.py",
                                       'first_missing_positive_entry.tsv',
                                       find_first_missing_positive))
