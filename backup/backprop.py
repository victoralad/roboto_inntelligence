#!/usr/bin/env python3.6
import numpy as np
import math
from copy import deepcopy
from collections import defaultdict
from forwardPass import forwardPass


def backprop(nn, X, Y):
    """
    Authors:    Matthew Gombolay <Matthew.Gombolay@cc.gatech.edu>
                Rohan Paleja <rpaleja3@gatech.edu>
                Letian Chen <letian.chen@gatech.edu>

    Date:       24 JUN 2020

    This function takes as input a neural netowrk, nn, and input-output
    pairs, <X,Y>, and computes the gradient of the loss for the neural
    network's current predictions. The code assumes that layers,
    {1,2,...,l-1}, have ReLU activations and the final layer has a linear
    activation function. The code ignores bias terms in the neural network.

    Inputs:

    nn            -   The weights and biases of the neural network. nn[i][0]
                    corresponds to the weights for the ith layer and
                    nn[i][1] corresponds to the biases for the ith layer
    X             -   This matrix is n x d matrix and contains the input
                   features for n examples, each with d features.
    Y             -   This term is an n x 1 vector of labels for n examples.

    Outputs:

    grad          -   The function outputs a cell of dimension numLayers x 1
                   where  numLayers is the number of layers in neural
               network, nn.

    """
    numLayers = len(nn)                                              # Get the number of layers of our neural network
    
    ######### forward pass ##########
    Y_hat, outputs, inputs = forwardPass(nn, X, return_output=True)  # Perform the forward pass on the neural network
    delta = [None] * numLayers                                       # Initialize the cell to store the error at level i
    for i in reversed(range(numLayers)):                             # Iterate over all layers
        if i == numLayers - 1:
            """
            The error for the output layer is simply the NEGATIVE difference
            between the targets, Y, and the predictions, Y_hat. Note that the
            use of this difference is based upon an assumption that we are
            applying an MSE loss to train our neural network.
            """
            # delta[i] = # INSERT CODE HERE
            delta[i] = -(Y - Y_hat)[0][0]
        else:

            """
            ``derivative'' is an  n^{(i)} x 1 vector where element
             j \in {1,..., n^{(i)}} is the derivative of the output of node j
             in layer i w.r.t. the input to that node. In other words, this
             term is the derivative of the activation function w.r.t. its
             inputs. We assume that the activation function for all non-final
             layers is ReLU, which is defined as

                                   /
             output = f(input) =   \ input   if  input >= 0
                                   /  0       otherwise
                                   \

             Therefore, the derivative is given by

                           /
             d output      \   1   if  input >= 0
             -------- =    |
             d input       /   0   otherwise
                           \
            """

			# MAY NEED TO WRITE HELPER CODE HERE BEFORE SETTING VALUE FOR delta
            delta_layer_i = [None] * np.array(inputs[i]).shape[0]
            for j in range(len(inputs[i])):
                if inputs[i][j][0] < 0:
                    delta_layer_i[j] = 0
                else:
                    delta_layer_i[j] = 1
            # delta[i] = # INSERT CODE HERE                # Compute the error term for layer i
            delta[i] = np.array(delta_layer_i).reshape(-1, 1)
            # print(np.array(delta[i]).shape)

    # Compute the gradients of all of the neural network's weights using the error term, delta
    grad = defaultdict(list)  # Initialize a cell array, where cell i contains the gradients for the weight matrix in layer i of the neural network
    
    # print(grad)
    for i in range(numLayers):
        if i == 0:
            # Weights for the first layer are updated using the examples, X.
            # grad[i].append(# INSERT CODE HERE) 
            # grad[i].append(# INSERT CODE HERE)
            grad[i].append(delta[i] * inputs[i].transpose())
            grad[i].append(delta[i])
        else:
            # Weights for subsequent layers are updated using the output of the previous layers.
            # grad[i].append(# INSERT CODE HERE) 
            # grad[i].append(# INSERT CODE HERE)

            grad[i].append(delta[i] * outputs[i - 1].transpose())
            print((delta[i] * outputs[i - 1]).shape)
            # print(delta[i].shape)
            grad[i].append(delta[i])
        if np.isnan(grad[i][0]).any() or np.isnan(grad[i][1]).any():
            print("Gradients/biases are nan")
            exit(0)
    # print(grad)  
    return grad

