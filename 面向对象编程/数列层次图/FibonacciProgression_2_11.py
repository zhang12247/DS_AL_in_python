from Progressio_2_8 import Progression


class FibonacciProgression(Progression):
    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current

if __name__ == '__main__':
    print('Default progression:')
    Progression().print_progression(10)

    print('FibonacciProgression with start values 4 and 6：')
    FibonacciProgression(4,6).print_progression(10)