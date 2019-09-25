from test_framework import generic_test


def square_root(k):
    # TODO - return 
    # return int(k**0.5)
    lo, hi = 0, k
    # candidate interval [lo,hi] has invariant:
    # everything before lo has square <= k, everything after hi has square > k
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid**2 <= k:
            lo = mid+1
        else:
            hi = mid-1
    # loop terminates when interval is EMPTY (ie lo>hi) - everything before lo has square <= k
    # return lo-1
    return lo - 1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
