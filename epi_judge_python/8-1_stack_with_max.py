from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import namedtuple

# 8.1 Implement a stack with Max api
# SOLUTION
    # use additional O(N) storage to track max from bottom of stack up to current element 
class Stack:
    ElementWithMax = namedtuple("ElementWithMax", ('x', 'max'))

    stack = []
    def empty(self):
        return len(self.stack) == 0

    def max(self):
        return self.stack[-1].max

    def pop(self):
        return self.stack.pop().x

    def push(self, x):
        if not self.stack:
            self.stack.append(self.ElementWithMax(x, x))
        else:
            prev_max = self.stack[-1].max
            self.stack.append(self.ElementWithMax(x, max(prev_max, x)))
        return


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("stack_with_max.py",
                                       'stack_with_max.tsv', stack_tester))
