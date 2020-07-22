# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 22:45:17 2020

@author: Christy
"""


import numpy as np # helps with the math
import pandas as pd
from sklearn import preprocessing
data = pd.read_csv("data/golf.csv")
le = preprocessing.LabelEncoder()

for x in data:
    data[x] = le.fit_transform(data[x])
inputs = data.drop('Play Golf',axis=1).values
outputs = data['Play Golf'].values
outputs=outputs.reshape((outputs.size, 1))

# create NeuralNetwork class
class NeuralNetwork:

    # intialize variables in class
    def __init__(self, input_array, output_array):
        self.inputs  = input_array
        self.outputs = output_array
        # initialize weights as .50 for simplicity
        #self.weights = np.array([[.50], [.50], [.50],[.50]])
        self.weights = np.random.random((input_array.shape[1],1))
        self.error_history = []
        self.epoch_list = []
        self.alpha = 0.1

    #activation function ==> S(x) = 1/1+e^(-x)
    def sigmoid(self, x, deriv=False):
        if deriv == True:
            return x * (1 - x)
        return 1 / (1 + np.exp(-x))

    # data will flow through the neural network.
    def feed_forward(self):
        self.hidden = self.sigmoid(np.dot(self.inputs, self.weights))
    # going backwards through the network to update weights
    def backpropagation(self):
        self.error  = self.outputs - self.hidden
        delta = self.error * self.sigmoid(self.hidden, deriv=True)
        self.weights += np.dot(self.inputs.T, delta)*self.alpha

    # train the neural net for 25,000 iterations
    def train(self, epochs=25000):
        for epoch in range(epochs):
            # flow forward and produce an output
            self.feed_forward()
            # go back though the network to make corrections based on the output
            self.backpropagation()    
            # keep track of the error history over each epoch
            self.error_history.append(np.average(np.abs(self.error)))
            self.epoch_list.append(epoch)

    # function to predict output on new and unseen input data                               
    def predict(self, new_input):
        prediction = self.sigmoid(np.dot(new_input, self.weights))
        if(prediction[0][0]<0.5):
            return 0,prediction[0][0]
        else:
            return 1,prediction[0][0]

# create neural network   
NN = NeuralNetwork(inputs, outputs)
# train neural network
NN.train()

# create two new examples to predict                                   
example = np.array([[2, 2, 0,1]])
example_2 = np.array([[0, 1, 1,0]])

# print the predictions for both examples                                   
print(NN.predict(example))
print(NN.predict(example_2))