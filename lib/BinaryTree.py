from .Tree import Tree


class BinaryTree(Tree):
    '''Abstract base class representing a binary tree structure'''

    # Additional abstract methods
    def left(self, p):
        '''Return a Position representing p's left child'''
        raise NotImplementedError('Must be implemented by subclass')

    def right(self, p):
        '''Return a position representing p's right child'''
        raise NotImplementedError('Must be implemented by subclass')


    # --- concrete methods implemented in this class ---
    def sibling(self, p):
        if self.is_root(p):
            return None
        
        parent = self.parent(p)
        if self.left(p) == p:
            return self.right(parent)
        return self.left(p)

    def children(self, p):
        '''Generate an iteration of Positions representing p's children'''
        if self.left(p) is not None:
            yield self.left(p)

        if self.right(p) is not None:
            yield self.right(p)