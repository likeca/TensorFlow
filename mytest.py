import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

def main():
    x = 3
    y = 5

    op1 = tf.add(x, y)
    op2 = tf.multiply(x, y)
    # op3 = tf.pow(op1, op2)
    # op4 = tf.pow(op2, op1)

    g = tf.Graph()
    with g.as_default():
        op1 = tf.add(x, y)
        op2 = tf.multiply(x, y)
        op = tf.add(op1, op2)

    # with tf.Session() as sess:
    #     print('op1: %s' % sess.run(op1))
    #     print('op2: %s' % sess.run(op2))
    #     print('op3: %s' % sess.run(op3))
    #     print('op4: %s' % sess.run(op4))

    with tf.Session(graph=g) as sess:
        sess.run(op)
        print('pow: %s' % sess.run(op))
        writer = tf.summary.FileWriter('./mygraph')
        writer.add_graph(sess.graph)

if __name__ == '__main__':
    main()

# python mytest.py
# tensorboard --logdir="mygraph"
