import itertools

itertools.accumulate(iterable) # - Make an iterator that returns accumulated sums.
    accumulate([1,2,3,4,5]) # --> 1 3 6 10 15
    accumulate([3,4,6,2,1,9,0,7,5,8], operator.mul) # --> [3,12,72,144,144,1296,0,0,0,0]
    accumulate([3,4,6,2,1,9,0,7,5,8], max) # --> [3,4,6,6,6,9,9,9,9,9]

itertools.combinations(iterable, r) # - r-length tuples, in sorted order, no repeated elements
    combinations('ABCD', 2) # --> AB AC AD BC BD CD
    combinations(range(4), 3) # --> 012 013 023 123

itertools.groupby(iterable, key=None) # - Make an iterator that returns consecutive keys and groups from the iterable.
    [k for k, g in groupby('AAAABBBCCDAABBB')] # --> A B C D A B
    [list(g) for k, g in groupby('AAAABBBCCD')] # --> AAAA BBB CC D

itertools.islice(iterable, stop)
itertools.islice(iterable, start, stop[, step]) # - Make an iterator that returns selected elements from the iterable
    islice('ABCDEFG', 2, None) # --> C D E F G 
    islice('ABCDEFG', 2, 4) # --> C D
    islice('ABCDEFG', 2, None) # --> C D E F G
    islice('ABCDEFG', 0, None, 2) # --> A C E G

itertools.product(*iterables, repeat=1) # - cartesian product, equivalent to a nested for-loop
    product(A, B) # --> ((x,y) for x in A for y in B)
    product('ABCD', 'xy') # --> Ax Ay Bx By Cx Cy Dx Dy
    product(range(2), repeat=3) # --> 000 001 010 011 100 101 110 111
    product('ABCD', repeat=2) # --> AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD