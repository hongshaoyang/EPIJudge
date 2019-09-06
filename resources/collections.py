import collections



deque = collections.deque(iterable) # create new deque

# queue behavior
deque.append(x) # append to right
deque.popleft(x) # pop from left 

# stack behavior
deque.append() # append to right
deque.pop() # pop from right