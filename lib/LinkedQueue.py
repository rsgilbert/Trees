class LinkedQueue:
    class _Node:
        def __init__(self, data, prev, next):
            self._next = next
            self._prev = prev
            self.data = data


    def __init__(self):
        self._trailer = self._Node(None, None, None)
        self._header = self._Node(None, self._trailer, None)
        self._trailer._next = self._header
        self._n = 0

    def __len__(self):
        return self._n

    def is_empty(self):
        return len(self) == 0

    def front(self):
        return self._header._prev.data

    def enqueue(self, data):
        node = self._Node(data, self._trailer, self._trailer._next)
        self._trailer._next._prev = node
        self._trailer._next = node
        self._n += 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyError('Empty queue')
        else:
            front = self.front()
            self._header._prev._prev._next = self._header
            self._header._prev = self._header._prev._prev
            self._n -= 1
            return front
        


class EmptyError(Exception):
    pass