from test_framework import generic_test
from test_framework.test_failure import TestFailure

from collections import OrderedDict

class LruCache2:
    def __init__(self, capacity):
        self.cache = {}
        self.time = 0
        self.capacity = capacity

    def hit(self, isbn):
        px = self.cache[isbn][0]
        self.cache[isbn] = (px, self.time)
        return px        

    def lookup(self, isbn):
        self.time += 1
        if isbn not in self.cache:
            return -1
        return self.hit(isbn)

    def insert(self, isbn, price):
        self.time += 1

        # TODO - you fill in here.
        if isbn in self.cache: # found, but don't change price
            self.hit(isbn)
        else: # not found
            # evict LRU
            if len(self.cache) == self.capacity:
                items = sorted((time, price, isbn) for (isbn, (price, time)) in self.cache.items())
                del self.cache[items[0][2]]

            self.cache[isbn] = (price, self.time)

    def erase(self, isbn):
        return self.cache.pop(isbn, None) is not None

class LruCache:
    '''Lru cache implemented with OrderedDict().
    - OrderedDict.popitem() returns and removes last inserted
    - OrderedDict.popitem(last=False) returns and removes first inserted
    '''

    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def lookup(self, isbn):
        if isbn not in self.cache:
            return -1
        px = self.cache.pop(isbn)
        self.cache[isbn] = px
        return px

    def insert(self, isbn, price):
        if isbn not in self.cache:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)
        else:
            price = self.cache.pop(isbn)
        
        self.cache[isbn] = price


    def erase(self, isbn):
        return self.cache.pop(isbn, None) is not None


def run_test(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure(
                    'Lookup: expected ' + str(cmd[2]) + ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure(
                    'Erase: expected ' + str(cmd[2]) + ', got ' + str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lru_cache.py", 'lru_cache.tsv',
                                       run_test))
