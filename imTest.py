from Gaussian import Gaussian
import numpy as np
import cv2
import matplotlib.pyplot as plt

# image index key
# [x][y][channel]
# bgr format

def getMuAndVar(values):

    mu = 0.0

    for value in values:
        mu += float(value)

    mu /= len(values)

    var = 0.0

    for value in values:
        var += pow((value - mu), 2)

    var /= (len(values) - 1)

    return mu, var


if __name__ == "__main__":

    imName = 'biden.png'

    kernelSize = 7
    kernelOffset = kernelSize // 2

    im = cv2.imread(imName)

    shape = im.shape
    height = shape[0]
    width = shape[1]
    channels = shape[2]
    
    cv2.imshow('Test', im)

    gaussRep = np.ndarray(shape = (width - kernelOffset, height - kernelOffset, channels), dtype = Gaussian)

    for i in range(1, height - kernelOffset):
        
        for j in range(1, width - kernelOffset):

            for c in range(0, channels):

                adjList = []

                for xOff in range(-kernelOffset, kernelOffset):
                    for yOff in range(-kernelOffset, kernelOffset):
                        adjList.append(im[i + xOff][j + yOff][c])

                mu, var = getMuAndVar(adjList)

                gaussRep[j - 1][i - 1][c] = Gaussian(mu, var)

    
    pixel = gaussRep[200][200]
    xs = np.arange(0, 255, 1)
    b = pixel[0].getCurve()
    g = pixel[1].getCurve()
    r = pixel[2].getCurve()

    fig, axs = plt.subplots(3)
    fig.suptitle('Color Gaussians')
    axs[0].plot(xs, r)
    axs[0].set(ylabel = 'Red')
    axs[0].set_yticklabels([])
    axs[1].plot(xs, g)
    axs[1].set(ylabel = 'Green')
    axs[1].set_yticklabels([])
    axs[2].plot(xs, b)
    axs[2].set(ylabel = 'Blue')
    axs[2].set_yticklabels([])

    plt.show()
    

    
