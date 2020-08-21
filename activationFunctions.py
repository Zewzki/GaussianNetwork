from math import sqrt, exp, sin

class ActivationFunction:

    def eval(self, value):
        pass


class Sigmoid(ActivationFunction):

    def eval(self, x):

        if isinstance(x, float):
            return exp(x) / (exp(x) + 1
        elif isinstance(x, Gaussian):
            print('Operation not yet defined')
            return None

class SigmoidPrime(ActivationFunction):

    def eval(self, x):

        if isinstance(x, float):
            return 1 / (1 + exp(-1 * x))
        elif isinstance(x, Gaussian):
            print('Operation not yet defined')
            return None
        

class HyperbolicTangent(ActivationFunction):

    def eval(self, x):

        if isinstance(x, float):
            return (exp(2x) - 1) / (exp(2x) + 1)
        elif isinstance(x, Gaussian):
            print('Operation not yet defined')
            return None

class Relu(ActivationFunction):

    def eval(self, x):

        if isinstance(x, float):
            return max(0, x)
        elif isinstance(x, Gaussian):
            print('Operation is not yet defined')
            return None
        
