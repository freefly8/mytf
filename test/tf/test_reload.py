import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

tf.set_random_seed(1)
np.random.seed(1)

# fake data
x = np.linspace(-1, 1, 100)[:, np.newaxis]  # shape (100, 1)
# noise = np.random.normal(0, 0.1, size=x.shape)
y = np.power(x, 2)  # shape (100, 1) + some noise
SESS_SAVE_PATH = "d:/temp/sess_store/1"


def reload():
    print('This is save')
    # build neural network
    tf_x = tf.placeholder(tf.float32, x.shape)  # input x
    tf_y = tf.placeholder(tf.float32, y.shape)  # input y
    l = tf.layers.dense(tf_x, 10, tf.nn.relu)  # hidden layer
    o = tf.layers.dense(l, 1)  # output layer
    loss = tf.losses.mean_squared_error(tf_y, o)  # compute cost
    train_op = tf.train.GradientDescentOptimizer(learning_rate=0.5).minimize(loss)

    sess = tf.Session()
    # sess.run(tf.global_variables_initializer())  # don't need initialize var in graph

    saver = tf.train.Saver()  # define a saver for saving and restoring

    saver.restore(sess, SESS_SAVE_PATH)
    # 接着训练
    for step in range(100):  # train
        sess.run(train_op, {tf_x: x, tf_y: y})

    # plotting
    pred, l = sess.run([o, loss], {tf_x: x, tf_y: y})
    plt.figure(1, figsize=(10, 5))
    # plt.subplot(121)
    plt.scatter(x, y)
    plt.plot(x, pred, 'r-', lw=5)
    plt.text(-1, 1.2, 'Save Loss=%.4f' % l, fontdict={'size': 15, 'color': 'red'})
    print("to show image")
    plt.show()


if __name__ == "__main__":
    reload()
