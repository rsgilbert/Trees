#### Template for implementing tree traversals using Euler tour traversal ###

class EulerTour:
    '''
    Abstract base class for performing Euler tour of a tree
    _hook_previsit and _hook_postvisit maybe overridden by subclasses 
    '''

    def __init__(self, tree):
        '''Prepare an Euler tour for a given tree'''
        self._tree = tree

    def tree(self):
        '''Returns reference to tree being traversed'''
        return self._tree

    
    def execute(self):
        '''Perform the tour and return any result from post visit of root'''
        if not self._tree.is_empty():
            return self._tour(self._tree.root(), 0, [])

    def _tour(self, p, d, path):
        '''
        Perform a tour of subtree rooted at position p
        p: position
        d: depth
        path: list of indices from root to p
        '''
        self._hook_previsit(p, d, path)
        results = []
        for (i, c) in enumerate(self._tree.children(p)):
            path.append(i)
            results.append(self._tour(c, d + 1, path))
            path.pop()
        return self._hook_postvisit(p, d, path, results)


    def _hook_previsit(self, p, d, path):
        '''What do I want to do before visiting the the subtrees'''
        pass

    def _hook_postvisit(self, p, d, path, results):
        '''What do I want to do with the results of visiting the subtrees'''
        pass



