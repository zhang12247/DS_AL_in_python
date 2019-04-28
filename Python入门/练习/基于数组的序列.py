import sys

if __name__ == '__main__':
    data = []
    for k in range(10):
        a = len(data)
        b = sys.getsizeof(data)
        print('Length:{0:3d};Size in bytes:{1:4d}'.format(a, b))
        data.append(None)
    print('data长度：',len(data))
    for k in range(10):
        a = len(data)
        b = sys.getsizeof(data)
        print('Length:{0:3d};Size in bytes:{1:4d}'.format(a, b))
        data.remove(data[-1])
        print(data)
        print(len(data))
