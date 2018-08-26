import tensorflow as tf
a=tf.Variable(1)
b=tf.Variable(2)
c=a+b
init=tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(c*3))