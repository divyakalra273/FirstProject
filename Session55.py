import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

print(tf.__version__)


hello = tf.constant("Hello from Tensorflow")
print(hello)