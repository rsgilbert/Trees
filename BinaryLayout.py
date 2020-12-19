from lib.BinaryEulerTour import BinaryEulerTour


class BinaryLayout(BinaryEulerTour):
    def __init__(self, tree):
        super().__init__(tree)
        self._n = 0

    def _hook_invisit(self, p, d, path):
        self._n += 1
        print(f'{self._n}, {d}')

        
