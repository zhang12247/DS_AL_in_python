class Empty(Exception):
    pass


class ArrayQueue:
    DEFAULT_CAPACITY = 1

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._size -= 1
        for i in range(len(self._data) - 1):
            self._data[i] = self._data[i + 1]
        self._data[-1] = None

        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = 0
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

    def __str__(self):
        return ' '.join(str(i) for i in self._data)


if __name__ == '__main__':
    S = ArrayQueue()
    S.enqueue(5)
    S.enqueue(3)
    print(S)
    S.dequeue()
    print(S)
    S.enqueue(10)
    print(S)
    S.enqueue(12)
    print(S)
    S.enqueue(13)
    S.enqueue(14)
    print(S)
    S.dequeue()
    print(S)
    S.enqueue(15)
    print(S)
    S.enqueue(18)
    print(S)
    S.dequeue()
    print(S)