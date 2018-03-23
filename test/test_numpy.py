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


def test_create():
    print(np.empty((3, 2, 3)))


def test_logic():
    a1 = np.arange(0, 20, 2)
    a2 = np.linspace(0, 20, 10)
    print(a1)
    print(a2)


# 点积
def test_dot():
    a1 = np.arange(1, 7, 1).reshape((2, 3))
    a2 = np.arange(1, 13, 1).reshape((3, 4))
    print(a1)
    print(a2)
    print(a1.dot(a2))


def test_split():
    a1 = np.arange(1, 10, 1).reshape((3, 3))
    print(a1)
    print("*" * 50)
    sub = a1[[0, 2]]
    print(sub)
    print("*" * 50)
    sub = a1[0]
    print(sub)
    print("*" * 50)
    sub = a1[[0, 2], 1:]
    print(sub)


def test_radom():
    import matplotlib.pyplot as plt
    count = 100
    print(np.random.rand(10))
    a1 = np.ones((count, 2))
    y=np.zeros(count)
    a2 = np.random.normal(a1,2)
    print(a1)
    print(a2)
    plt.scatter(a2[:, 0], y,s=10)
    plt.show()


def tmp():
    n_data = np.ones((10, 2))
    print("n_data:", n_data)
    x0 = np.random.normal(2 * n_data, 1)  # class0 x shape=(100, 2)
    print("x0:", x0)
    y0 = np.zeros(10)  # class0 y shape=(100, 1)
    print("y0:", y0)
    x1 = np.random.normal(-2 * n_data, 1)  # class1 x shape=(100, 2)
    print("x1:----", x1)
    y1 = np.ones(10)  # class1 y shape=(100, 1)
    x = np.vstack((x0, x1))  # shape (200, 2) + some noise
    y = np.hstack((y0, y1))  # shape (200, )
    x2 = np.random.normal(-2 * y0, 1)


if __name__ == "__main__":
    # test_stack1()
    # test_stack2()
    # test_hstack()
    # test_vstack()
    # test_create()
    # test_logic()
    # test_dot()
    # test_split()
    test_radom()
    # tmp()
