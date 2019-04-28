class Empty(Exception):
    pass


class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()


def reverse_file(filename):
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()

    output = open(filename, 'w')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()


def is_matched(expr):
    left = '{[('
    right = '}])'
    S = ArrayStack()
    for c in expr:
        if c in left:
            S.push(c)
        elif c in right:
            if S.is_empty():
                return False
            if right.index(c) != left.index(S.pop()):
                return False
    return S.is_empty()


def is_matched_html(raw):
    S = ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j + 1)
        if k == -1:
            return False
        tag = raw[j + 1:k]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            a= tag[1:]
            b=S.pop()
            print(1,a,b)
            if a!= b:
                return False
        j = raw.find('<', k + 1)
    return S.is_empty()


if __name__ == '__main__':
    print(is_matched_html(
        "<div id=\"toast-container\" ng-class=\"[config.position, config.animation]\" toaster-options=\"{'position-class': 'toast-bottom-right', 'toaster-id': 2, 'limit': 1}\" class=\"ng-scope toast-bottom-right\"></div>"))
