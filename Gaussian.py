import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
from math import pi
from math import exp

def printGaussianList(arr, name):

    print('{0}:'.format(name))
    for xs in arr:
        for cell in xs:
            print(cell, end = '\t')
        print()
    print()

class Gaussian:

    def __init__(self, mu = 0.0, sigma = 0.0, scalingFactor = 1.0):
        self.scalingFactor = scalingFactor
        self.mu = mu
        self.sigma = sigma
        if self.sigma == 0:
            self.sigma = .00001

    def __str__(self):
        return "N({0}, {1})".format(self.mu, self.sigma)
    
    def __add__(self, other):

        # add constant
        if isinstance(other, float):
            mu = self.mu + other
            sigma = self.sigma
            return Gaussian(mu, sigma)

        # sum two Gaussians
        elif isinstance(other, Gaussian):
            mu = self.mu + other.mu
            sigma = self.sigma + other.sigma
            return Gaussian(mu, sigma)

        else:
            print("Invalid Operation: {0} + {1}".format(type(self), type(other)))
            return Gaussian()

    def __sub__(self, other):

        # sub constant
        if isinstance(other, float):
            mu = self.mu - other
            sigma = self.sigma
            return Gaussian(mu, sigma)

        # sub one gaussian from another
        elif isinstance(other, Gaussian):
            mu = self.mu - other.mu
            sigma = self.sigma - other.sigma
            sigma = max(sigma, 0)
            return Gaussian(mu, sigma)

        else:
            print("Invalid Operation: {0} - {1}".format(type(self), type(other)))
            return Gaussian()
        
    def __mul__(self, other):

        # scalar multiplication
        if isinstance(other, float):
            mu = self.mu * other
            sigma = self.sigma * pow(other, 2)
            return Gaussian(mu, sigma)

        # product of two gaussians
        elif isinstance(other, Gaussian):

            mu = self.mu * pow(other.sigma, 2)
            mu += other.mu * pow(self.sigma, 2)
            mu /= (pow(other.sigma, 2) + pow(self.sigma, 2))

            sigma = pow(self.sigma, 2) * pow(other.sigma, 2)
            sigma /= pow(self.sigma, 2) + pow(other.sigma, 2)

            return Gaussian(mu, sigma)

        else:
            print("Invalid Operation: {0} * {1}".format(type(self), type(other)))
            return Gaussian()

    def __truediv__(self, other):

        # scalar division
        if isinstance(other, float):
            mu = self.mu / other
            sigma = self.sigma / pow(other, 2)
            return Gaussian(mu, sigma)

        # gaussian division
        elif isinstance(other, Gaussian):
            print("Operation not yet defined")
            return Gaussian()

        else:
            print("Invalid Operation: {0} / {1}".format(type(self), type(other)))
            return Gaussian()

    def __pow__(self, other):

        if isinstance(other, Gaussian):

            var1 = pow(self.sigma, 2)
            var2 = pow(other.sigma, 2)

            mu = ((self.mu * var2) + (other.mu * var1)) / (var1 + var2)
            sigma = sqrt((var2 * var1) / (var1 + var2))
            scalingFactor = (1.0 / sqrt(2 * pi * (var1 + var2))) * exp(-1.0 * (pow(other.mu - self.mu, 2) / (2 * (var1 + var2))))
            return Gaussian(mu, sigma, scalingFactor)

        else:
            print("Invalid input type: {0}".format(type(other)))
            return None

    def evaluate(self, x):
        
        return (self.scalingFactor / (self.sigma * sqrt(2 * pi))) * exp((-1/2) * pow(((x - self.mu) / self.sigma), 2))
    

    def getCurve(self, domain = (0, 255), step = 1):

        xs = np.arange(domain[0], domain[1], step)
        
        ys = []

        for x in xs:
            ys.append(self.evaluate(x))

        return ys

    def disp(self, domain = None):

        if domain is None:
            domain = (self.mu - (3 * self.sigma), self.mu + (3 * self.sigma))

        if not isinstance(domain, tuple):
            print("Incorrect usage: requires (xMin, xMax)")
            return
        if not len(domain) == 2:
            print("Incorrect usage: requires (xMin, xMax)")
            return

        step = .5
        xs = np.arange(domain[0], domain[1], step)
        y = []
        for x in xs:
            y.append(self.evaluate(x))
        
        plt.figure()
        plt.plot(xs, y)
        plt.show()
