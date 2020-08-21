from Gaussian import Gaussian
from Gaussian import printGaussianList
import numpy as np
from random import random, gauss

bias = Gaussian(1.0, .0001)

def relu(arr):

    for xs in arr:
        for x in xs:
            if x.mu < 0:
                x.mu = 0

    return arr

if __name__ == "__main__":

    hiddenWidth = 5
    inputSize = 3

    # 1 x 4
    X = np.ndarray(shape = (1, inputSize + 1), dtype = Gaussian)
    for xs in X:
        for i in range(0, len(xs) - 1):
            xs[i] = Gaussian(i + 1, 2)
        xs[len(xs) - 1] = bias

    #print('X Shape: {0}'.format(X.shape))

    printGaussianList(X, 'X')

    # 5 x 4
    w1 = np.zeros(shape = (hiddenWidth, inputSize + 1))

    for i in range(0, len(w1)):
        for j in range(0, len(w1[i])):
            #w1[i][j] = j + .7 * (i - 2)
            w1[i][j] = gauss(0, 1)

    #print('W1 Shape: {0}'.format(w1.shape))
    
    # 1 x 6
    w2 = np.zeros(shape = (1, hiddenWidth + 1))

    for i in range(0, len(w2)):
        for j in range(0, len(w2[i])):
            #w2[i][j] = .7 * j
            w2[i][j] = gauss(0, 1)

    #print('W2 Shape: {0}'.format(w2.shape))

    # Begin forward pass

    # 5 x 1
    b = np.transpose(np.matmul(X, np.transpose(w1)))
    #print('B Shape: {0}'.format(b.shape))


    z = relu(b)
    #print('Z Shape: {0}'.format(z.shape))

    printGaussianList(z, 'Z')

    z1 = np.append(z, bias)
    z1 = np.expand_dims(z1, axis = 1)
    #print('Z1 Shape: {0}'.format(z1.shape))

    a = np.transpose(np.matmul(np.transpose(z1), np.transpose(w2)))
    #print('A Shape: {0}'.format(a.shape))

    printGaussianList(a, 'A')

    
    
