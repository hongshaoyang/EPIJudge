
# a binary search tree
class BST():
    def __init__(self, val):
        self.l = None
        self.r = None
        self.value = val
    
    def insert(self, val):
        if (val > self.value):
            if not self.r:
                self.r = BST(val)
            else:
                self.r = self.r.insert(val)
        if 