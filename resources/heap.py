import itertools
import heapq

'''
Take a sequence of strings, in "streaming" fashion (ie one pass).
Compute the k longest strings in the sequence. No need to order the k strings.

Solution:
Use a min-heap (NOT A MAX-HEAP!) Supports efficient
    - findMin in O(1)
    - removeMin in O(logN)
    - insert() in O(logN)


heapq.heapify(L)            - transform list L into a min-heap, in-place, in O(N) time

heapq.heappush(h, i)        - push i to heap
heapq.heappop(h)            - pop smallest item from heap and return
h[0]                        - access smallest item from heap, without popping
heapq.heappushpop(h, item)  - push item then pop and return smallest item

heapq.nlargest(n, L)
heapq.nsmallest(n, L) - return n largest/smallest elem in iterabl
'''

def top_k(k, stream):
    # entries are compared by their length
    min_heap = [(len(s), s) for s in itertools.islice(stream, k)]
    heapq.heapify(min_heap)

    for next_string in stream:
        # push next_string, and pop shortest string
        heapq.heappushpop(min_heap, (len(next_string), string))

    return [p[1] for p in heapq.nsmallest(k, min_heap)]