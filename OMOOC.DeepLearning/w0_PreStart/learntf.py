import tensorflow as tf

c = tf.constant("hello world")
session = tf.Session()
print(session.run(c))
