import numpy as np
from Gaussian import Gaussian

if __name__ == "__main__":

    g1 = Gaussian(15, 22)
    g1.disp((0, 255))
    g2 = Gaussian(3, 5)
    
    const = 5.0

    addConst = g1 + const
    print("Add Constant: ", addConst)
    
    addGauss = g1 + g2
    print("Add Gaussians: ", addGauss)
    
    addGaussRev = g2 + g1
    print("Add Gaussians Reverse: ", addGaussRev)

    

    subConst = g1 - const
    print("Subtract Constant: ", subConst)
    
    subGauss = g1 - g2
    print("Subtract Gaussian: ", subGauss)



    multConst = g1 * const
    print("Multiply Constant: ", multConst)
    
    multGauss = g1 * g2
    print("Multiply Gaussians: ", multGauss)
    
    multGaussRev = g2 * g1
    print("Multiply Gaussianse Reverse: ", multGaussRev)



    divConst = g1 / const
    print("Divide Constant: ", divConst)
    
    divGauss = g1 / g2
    print("Divide Gaussians: ", divGauss)

    
