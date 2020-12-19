from .EulerTour import EulerTour


class BinaryEulerTour(EulerTour):
    def _tour(self, p, d, path):
        '''
        Perform a tour of subtree rooted at position p
        p: position
        d: depth
        path: list of indices from root to p
        '''
        self._hook_previsit(p, d, path)
        results = [None, None]
        if self._tree.left(p):
            path.append(0)
            results.append(self._tour(self._tree.left(p), d + 1, path))
            path.pop()
        self._hook_invisit(p, d, path)
        if self._tree.right(p):
            path.append(1)
            results.append(self._tour(self._tree.right(p), d + 1, path))
            path.pop()
        return self._hook_postvisit(p, d, path, results)


    def _hook_invisit(self, p, d, path):
        pass
