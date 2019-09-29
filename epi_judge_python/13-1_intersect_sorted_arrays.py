from test_framework import generic_test
import bisect

def intersect_two_sorted_arrays(A, B):
    i, j, res = 0, 0, []

    while i < len(A) and j < len(B):
        a, b = A[i], B[j]

        if a < b:
            i += 1
        elif a > b:
            j += 1
        else:
            if len(res)== 0 or res[-1] != a:
                res.append(a)
            i += 1
            j += 1
    return res
    



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
