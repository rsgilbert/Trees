from .LinkedQueue import LinkedQueue
class Tree:
    class Position:
        '''An abstraction representing the location of a single element'''

        def element(self):
            raise NotImplementedError('Must be implemented by subclass')

        def __eq__(self, other):
            raise NotImplementedError('Must be implemented by subclass')

        def __ne__(self, other):
            return not self == other


    # ---- Abstract methods that concrete subclass must implement ----        
    def root(self):
        raise NotImplementedError('Must be implemented by subclass')

    def parent(self, p):
        raise NotImplementedError('Must be implemented by subclass')

    def num_children(self, p):
        raise NotImplementedError('Must be implemented by subclass')

    def children(self, p):
        raise NotImplementedError('Must be implemented by subclass')

    def __len__(self):
        raise NotImplementedError('Must be implemented by subclass')

    def positions(self):
        raise NotImplementedError('Must be implemented by subclass')

    # --- Concrete methods implemented by Tree
    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        if self.is_root(p):
            return 0
        return 1 + self.depth(self.parent(p))


    def _height(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height(c) for c in self.children(p))

    def height(self, p = None):
        if p is None:
            p = self.root()
        return self._height(p)

    
    def __iter__(self):
        '''Generate an iteration of the tree's elements'''
        for p in self.positions():
            yield p.element()

    
    ### Traversal algorithms ###

    # Preorder
    # Visit root of subtree then traverse its children

    def _subtree_preorder(self, p):
        yield p
        for child_p in self.children(p):
            for child_other in self._subtree_preorder(child_p):
                yield child_other

    def preorder(self):
        if not self.is_empty():
            return self._subtree_preorder(self.root())
   

    # Postorder
    # Traverse subtrees before visiting the root

    def _subtree_postorder(self, p):
        for child_p in self.children(p):
            for child_other in self._subtree_postorder(child_p):
                yield child_other
        yield p

    def postorder(self):
        return self._subtree_postorder(self.root())


    # Breadth-first search
    # Visit items in row after row 

    def _subtree_breadthfirst(self, p):
        if not self.is_empty():
            Q = LinkedQueue()
            Q.enqueue(p)
            while not Q.is_empty():
                position = Q.dequeue()
                [Q.enqueue(child_pos) for child_pos in self.children(position)]
                yield position
        
    # Breadthfirst traversal starting with the root
    def breadthfirst(self):
        return self._subtree_breadthfirst(self.root())