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


    # Inorder Traversal
    # Visit position between traversals of its left and right subtrees
    def _subtree_inorder(self, p):
        if self.left(p):
            # yield the results of inorder traversal on its left subtree
            for pos in self._subtree_inorder(self.left(p)):
                yield pos
        yield p
        if self.right(p):
            # yield the results of inorder traversal on its right subtree
            for pos in self._subtree_inorder(self.right(p)):
                yield pos


    def inorder(self):
        '''Perform inorder traversal on the root'''
        return self._subtree_inorder(self.root())


    # override inherited version of positions to make inorder default
    def positions(self):
        return self.inorder()

