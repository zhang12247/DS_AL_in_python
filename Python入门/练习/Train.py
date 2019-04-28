import sys
sys.setrecursionlimit(1000000)

"""编写一个python函数is_multiple(n,m)用来接收2个整数值n和m，如果n是m的倍数，即存在整数使得n=mi，那么函数返回True，否则返回False"""


def is_multiple(n, m):
    return n % m == 0


"""编写函数is_even(k)，用来接收整数k，如果k是整数返回True，反之返回False，不能使用乘法，除法和取余操作"""


def is_even(k):
    k = abs(k)
    while k > 1:
        k -= 2
    return k == 0


"""编写一个python函数minmax(data)，用来在数的序列中找出最小数和最大数，并以一个长度为2的元组的形式返回。不能使用min和max函数"""


def minmax(data):
    mind, maxd = data[0], data[0]
    for item in data:
        if mind >= item:
            mind = item
        if maxd <= item:
            maxd = item
    return (mind, maxd)


"""接受正整数n，返回1~n的平方和"""


def square_n(n):
    count = 0
    for i in range(n + 1):
        count += i ** 2

    return count


"""基于python解析语法和内置sum，写一个单独的命令来计算R-1.4中的和"""


def sum_square(n):
    return sum([x ** 2 for x in range(n + 1) if x % 2 > 0])


def list_create():
    return list(map(lambda x: 2 ** x, range(9)))


def bad_fibonacci(n):
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n - 2) + bad_fibonacci(n - 1)



def good_fibonacci(n):
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n - 1)
        return (a + b, a)

def move(n,a,b,c):
    if n==1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

if __name__ == '__main__':
    # print(bad_fibonacci(100))
    # print(good_fibonacci(1000))
    move(5,'A','B','C')
