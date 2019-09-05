import heapq
from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays):
    # push zeroth elements of all arrs to minheap
    min_heap = [(arr.pop(0), i) for i, arr in enumerate(sorted_arrays) if arr]
    heapq.heapify(min_heap)

    res = []
    while any(sorted_arrays):
        # pop the minheap and add the next element from that arr to the list
        num, idx = heapq.heappop(min_heap)
        res.append(num)
        if sorted_arrays[idx]:
            heapq.heappush(min_heap, (sorted_arrays[idx].pop(0), idx))
    
    # continue popping the minheap until it's done
    while min_heap:
        res.append(heapq.heappop(min_heap)[0])
    return res




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
