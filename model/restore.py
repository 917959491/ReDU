import tensorflow as tf
import six.moves.cPickle as pickle
from model import config as cf
import numpy as np
import math

def get_batch(x, L, y, sz, time, n_time_interval, step, batch_size, num_step):
    batch_y = np.zeros(shape=(batch_size, 1))
    batch_x = []
    batch_L = []
    batch_time_interval_index = []
    batch_rnn_index = []
    start = step * batch_size % len(x)
    for i in range(batch_size):
        id = (i + start) % len(x)
        batch_y[i, 0] = y[id]
        batch_L.append(L[id].todense())
        temp_x = []
        for m in range(len(x[id])):
            temp_x.append(x[id][m].todense())
        batch_x.append(temp_x)
        batch_time_interval_index_sample = []

        for j in range(sz[id]):
            temp_time = np.zeros(shape=(n_time_interval))
            k = int(math.floor(time[id][j] / config.time_interval))
            temp_time[k] = 1
            batch_time_interval_index_sample.append(temp_time)
        if len(batch_time_interval_index_sample) < num_step:
            for i in range(num_step - len(batch_time_interval_index_sample)):
                temp_time_padding = np.zeros(shape=(n_time_interval))
                batch_time_interval_index_sample.append(temp_time_padding)
                i = i + 1
        batch_time_interval_index.append(batch_time_interval_index_sample)
        rnn_index_temp = np.zeros(shape=(config.n_steps))
        rnn_index_temp[:sz[id]] = 1
        batch_rnn_index.append(rnn_index_temp)

    return batch_x, batch_L, batch_y, batch_time_interval_index, batch_rnn_index


n_steps = 100
tf.flags.DEFINE_integer("n_steps", n_steps, "num of step.")
tf.flags.DEFINE_integer("time_interval", cf.time_interval, "the time interval")
tf.flags.DEFINE_integer("n_time_interval", cf.n_time_interval, "the number of  time interval")
tf.flags.DEFINE_integer("batch_size", 16, "batch size.")

config = tf.flags.FLAGS

saver = tf.train.import_meta_graph("save/model.ckpt-400.meta")

with tf.Session() as sess:
    saver.restore(sess, "./save/model.ckpt-400")
    graph = tf.get_default_graph()
    # with open("graph12.1.txt", "a", encoding='utf-8') as file:
    #     for n in tf.get_default_graph().as_graph_def().node:
    #         print(n.name)
    #         file.write(n.name+"\n")
    # file.close()

    # ops = graph.get_operations()
    # with open("ops12.2.txt", "a", encoding='utf-8') as file1:
    #     for n in ops:
    #         file1.write(n+'\n')
    # file1.close()


    x=graph.get_tensor_by_name('x:0')
    laplacian = graph.get_tensor_by_name('laplacian:0')
    y = graph.get_tensor_by_name('y:0')
    time_interval_index = graph.get_tensor_by_name('time:0')
    rnn_index = graph.get_tensor_by_name('rnn_index:0')
    op_to_pred = graph.get_tensor_by_name('dense_1/pred_porb:0')

    id_test, x_test, L_test, y_test, sz_test, time_test, _, _ = pickle.load(
        open(cf.test_pkl, 'rb'))
    batch_size=config.batch_size
    n_steps = 100
    predict_result=[]
    for test_step in range(int(len(y_test) / batch_size + 1)):
        test_x, test_L, test_y, test_time, test_rnn_index = get_batch(
            x_test,
            L_test,
            y_test,
            sz_test,
            time_test,
            config.n_time_interval,
            test_step,
            batch_size,
            n_steps)
        # result = sess.run(op_to_pred, feed_dict={
        #     x: test_x,
        #     laplacian: test_L,
        #     y: test_y,
        #     time_interval_index: test_time,
        #     rnn_index: test_rnn_index})
        predict_result.extend(sess.run(op_to_pred, feed_dict={
            x: test_x,
            laplacian: test_L,
            y: test_y,
            time_interval_index: test_time,
            rnn_index: test_rnn_index}))
    pickle.dump((predict_result), open(
        "final_prediction_result_" + str(12.2) + "_CasCN", 'wb'))
    print('finish!')




