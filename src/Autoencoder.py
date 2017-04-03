import tensorflow as tf
import numpy as np

class InputLayer:
    def __init__(self, outSize):
        self.outSize = outSize
        self.input = tf.placeholder(tf.float32, [None, outSize])

    def printLayerShape(self):
        print("\nThe shape of input is: ", self.input.get_shape())

class HiddenLayer:
    def __init__(self, outSize, layerInput):
        self.layerInput = layerInput
        self.outSize = outSize
        num_rows, num_cols = x.get_shape().as_list()
        self.inSize = num_rows
     
        self.w1 = tf.Variable('w1', 
                              shape = [self.inSize, self.outSize],
                              initializer = tf.contrib.layers.xavier_initializer(),
                              regularizer = tf.contrib.layers.l2_regularizer(0.01))
        self.b1 = tf.Variable(tf.zeros(len(self.self.outSize)))
        self.w2 = tf.Variable('w2',
                              shape = [self.outSize, self.inSize],
                              initializer = tf.contrib.layers.xavier_initializer(),
                              regularizer = tf.contrib.layers.l2_regularizer(0.01))
        self.b2 = tf.Variable(tf.zeros(self.inSize))
        
        self.z1 = tf.matmul(self.layerInput, self.w1) + self.b1
        self.y1 = tf.nn.relu(self.z1)
        self.z2 = tf.matmul(self.y1, self.w2) + self.b2
        self.y2 = tf.nn.relu(self.z2)

    def printLayerShape(self):
        print("\nThe shape of the x is: ", self.x.get_shape())
        print("The shape of w1 is: ", self.w1.get_shape())
        print("The shape of b1 is: ", self.b1.get_shape())
        print("The shape of w2 is: ", self.w2.get_shape())
        print("The shape of b2 is: ", self.b2.get_shape())
        print("The shape of z1 is: ", self.z1.get_shape())
        print("The shape of y1 is: ", self.y1.get_shape())
        print("The shape of z2 is: ", self.z2.get_shape())
        print("The shape of y2 is: ", self.y2.get_shape())

class OutputLayer:
    def __init__(self, outSize, layerInput):
        self.outSize = outSize
        self.layerInput = layerInput

        self.wo = tf.Variable('wo', 
                              shape = [self.inSize, self.outSize],
                              initializer = tf.contrib.layers.xavier_initializer(),
                              regularizer = tf.contrib.layers.l2_regularizer(0.01))
        self.bo = tf.Variable(tf.zeros(len(self.outSize)))
        self.zo = tf.matmul(layerInput, self.wo) + self.bo
        self.yo = tf.nn.relu(self.zo)

    def printLayerShape(self):
        print("\nThe shape of x is: ", layerInput.get_shape())
        print("The shape of wo is: ", self.wo.get_shape())
        print("The shape of bo is: ", self.bo.get_shape())
        print("The shape of zo is: ", self.zo.get_shape())
        print("The shape of yo is: ", self.yo.get_shape())