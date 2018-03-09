import numpy as np


# 一维变二维  http://blog.csdn.net/csdn15698845876/article/details/73380803
def test_stack1():
    a = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]
         ]
    print("列表a如下：")
    print(a)

    print("增加一维，新维度的下标为0")
    c = np.stack(a, axis=0)
    print(c)

    print("增加一维，新维度的下标为1")
    c = np.stack(a, axis=1)
    print(c)


# 二维变三维  http://blog.csdn.net/csdn15698845876/article/details/73380803
def test_stack2():
    a = [[1, 2, 3],
         [4, 5, 6]]
    b = [[1, 2, 3],
         [4, 5, 6]]
    c = [[1, 2, 3],
         [4, 5, 6]]
    print("a=", a)
    print("b=", b)
    print("c=", c)

    print("增加一维，新维度的下标为0")
    d = np.stack((a, b, c), axis=0)
    print(d)

    print("增加一维，新维度的下标为1")
    d = np.stack((a, b, c), axis=1)
    print(d)
    print("增加一维，新维度的下标为2")
    d = np.stack((a, b, c), axis=2)
    print(d)


# 水平(按列顺序)把数组给堆叠起来
def test_hstack():
    a = [1, 2, 3]
    b = [4, 5, 6]
    print(np.hstack((a, b)))

    a = [[1], [2], [3]]
    b = [[1], [2], [3]]
    c = [[1], [2], [3]]
    d = [[1], [2], [3]]
    print(np.hstack((a, b, c, d)))


# 垂直(按列顺序)把数组给堆叠起来
def test_vstack():
    a = [1, 2, 3]
    b = [4, 5, 6]
    print(np.vstack((a, b)))
    a = [[1], [2], [3]]
    b = [[4], [5], [6]]
    c = [[7], [8], [9]]
    d = [[1], [2], [3]]
    print(np.vstack((a, b, c, d)))


if __name__ == "__main__":
    # test_stack1()
    # test_stack2()
    # test_hstack()
    test_vstack()
