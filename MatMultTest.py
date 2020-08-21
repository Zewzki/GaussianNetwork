from Gaussian import Gaussian
import numpy as np
from random import random

def printGaussianArray(arr, name):
    print(name)

    print('[[', end = '')

    for row in arr:
        for cell in row:
            print(cell, end = '\t')
        print(']')
    print(']')


if __name__ == "__main__":

    muMax = 255.0
    varMax = 10.0

    arr1 = np.ndarray(shape = (3, 3), dtype = Gaussian)
    arr2 = np.ndarray(shape = (3, 3), dtype = Gaussian)

    for i in range(0, 3):
        for j in range(0, 3):
            
            mu1 = float(int(random() * muMax))
            var1 = random() * varMax
            arr1[i][j] = Gaussian(mu1, var1)

            mu2 = float(int(random() * muMax))
            var2 = random() * varMax
            arr2[i][j] = Gaussian(mu2, var2)

    arr3 = arr1 * arr2

    printGaussianArray(arr1, "Array 1")
    printGaussianArray(arr2, "Array 2")
    printGaussianArray(arr3, "Array 3")
    
