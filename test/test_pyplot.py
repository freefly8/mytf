# -- coding:utf-8 --
import numpy as np
from matplotlib import rcParams
import matplotlib.pyplot as plt
import math

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['simHei']
rcParams['axes.unicode_minus'] = False


def test_set_params():
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['simHei']

    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], label='张业勇')

    ax.legend()
    plt.show()


def test_figure():
    fig = plt.figure(figsize=(8, 6))
    #     创建对象
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    # 拆线图
    plt.plot(np.random.random(50).cumsum(), "b--")
    # 直方图
    ax1.hist(np.random.random(300), bins=20, color="b", alpha=0.3)
    # &点图
    ax2.scatter(np.arange(30), np.arange(30) + 2 * np.random.randn(30))
    plt.xlabel("X")
    plt.ylabel("y")
    plt.title("test by zyy")
    plt.legend()
    plt.show()


def test_plot():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    z = np.cos(2 * x)
    plt.figure()
    plt.plot(x, y, label="$sin(x)$", color="r", linestyle="dashed",
             marker="o")
    plt.plot(x, z, "b--", label="$cos(x)$")
    plt.xlabel("X")
    plt.ylabel("y")
    plt.title("test by zyy")
    plt.grid(True)
    plt.legend()
    plt.show()


def test_set():
    plt.figure()
    r = range(5)
    line = plt.plot(r)[0]  # plot函数返回的是一个列表,因为可以同时画多条线的哦;
    line.set_color('r')
    line.set_linewidth(2.0)
    plt.show()
    # ————————————  或者  ————————————
    plt.figure()
    line = plt.plot(range(5))[0]  # plot函数返回的是一个列表,因为可以同时画多条线的哦;
    line.set(color='g', linewidth=2.0)
    plt.show()
    # ————————————  或者 ————————————
    plt.figure()
    lines = plt.plot(range(5), range(5), range(5), range(8, 13))  # plot函数返回一个列表;
    plt.setp(lines, color='g', linewidth=2.0)  # setp函数可以对多条线进行设置的;
    plt.show()


def test_fig():
    plt.figure(1)  # 建立figure(1)
    plt.figure(2)  # 建立figure(2)
    ax1 = plt.subplot(2, 1, 1)
    ax2 = plt.subplot(2, 1, 2)
    plt.sca(ax1)  # 切换到子图1
    plt.sca(ax2)  # 切换到子图2
    plt.figure(1)  # 切换到figure(1),它不是重建哦；


def test_scatter():
    # Generating a Gaussion dataset:
    # creating random vectors from the multivariate normal distribution
    # given mean and covariance
    mu_vec1 = np.array([0, 0])
    cov_mat1 = np.array([[2, 0], [0, 2]])

    x1_samples = np.random.multivariate_normal(mu_vec1, cov_mat1, 100)
    x2_samples = np.random.multivariate_normal(mu_vec1 + 0.2, cov_mat1 + 0.2, 100)
    x3_samples = np.random.multivariate_normal(mu_vec1 + 0.4, cov_mat1 + 0.4, 100)

    # x1_samples.shape -> (100, 2), 100 rows, 2 columns

    plt.figure(figsize=(8, 6))

    plt.scatter(x1_samples[:, 0], x1_samples[:, 1], marker='x',
                color='blue', alpha=0.7, label='x1 samples')
    # plt.scatter(x2_samples[:, 0], x1_samples[:, 1], marker='o',
    #             color='green', alpha=0.7, label='x2 samples')
    # plt.scatter(x3_samples[:, 0], x1_samples[:, 1], marker='^',
    #             color='red', alpha=0.7, label='x3 samples')
    plt.title('Basic scatter plot')
    plt.ylabel('variable X')
    plt.xlabel('Variable Y')
    plt.legend(loc='upper right')

    plt.show()


def test_scatter2():
    from matplotlib.font_manager import FontProperties
    font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)  # 解决中文乱码
    # 产生测试数据
    x = np.arange(1, 10)
    y = x
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    # 设置标题
    ax1.set_title('Scatter Plot  张业勇', fontproperties=font_set)
    # 设置X轴标签
    plt.xlabel(u'横轴', fontproperties=font_set)
    # 设置Y轴标签
    plt.ylabel('Y')
    # 画散点图
    ax1.scatter(x, y, c='r', marker='x')
    # 设置图标
    plt.legend('x1')
    # 显示所画的图
    plt.show()


def test_drow_yuan():
    fig = plt.figure(0)
    degree = np.random.rand(50) * np.pi * 2
    x_1 = np.cos(degree) * np.random.rand(50)
    y_1 = np.sin(degree) * np.random.rand(50)
    x_2 = np.cos(degree) * (1 + np.random.rand(50))  # 半径大1
    y_2 = np.sin(degree) * (1 + np.random.rand(50))  # 半径大1

    # x_3 和 y_3 就是切分线
    t = np.linspace(0, np.pi * 2, 50)  # 等分50份
    x_3 = np.cos(t)
    y_3 = np.sin(t)

    plt.scatter(x_1, y_1, c='red', s=50, alpha=0.4, marker='o')  # 散点图
    plt.scatter(x_2, y_2, c='black', s=50, alpha=0.4, marker='o')
    plt.plot(x_3, y_3)  # 是个圆
    plt.show()


def test_drow_yuan2():
    angles_circle = [i * math.pi / 180 for i in range(0, 360)]  # i先转换成double
    # angles_circle = [i/np.pi for i in np.arange(0,360)]             # <=>
    # angles_circle = [i/180*pi for i in np.arange(0,360)]    X
    R1 = 2
    R2 = 1

    x = R1 * np.cos(angles_circle)
    y = R1 * np.sin(angles_circle)
    plt.plot(x, y, 'r')
    x = R2 * np.cos(angles_circle)
    y = R2 * np.sin(angles_circle)
    plt.plot(x, y, 'b')

    plt.axis('equal')
    plt.axis('scaled')
    plt.show()


def test_drow_bar():
    plt.bar(1, 1)
    plt.show()


if __name__ == "__main__":
    # test_set_params()
    # test_figure()
    # test_plot()
    # test_set()
    # test_scatter()

    #     画圆
    # test_drow_yuan2()
    #     画直方图
    test_drow_bar()
