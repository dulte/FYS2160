import numpy as np
import matplotlib.pyplot as plt
from scipy.special import binom

def numberOfMacroStates(NA,NB,q):

    numMacrostates = np.zeros(q+1)
    probability = np.zeros_like(numMacrostates)

    for i in range(q+1):
        qa = i
        qb = q-qa

        numMacrostates[i] = binom(qa + NA -1,qa)*binom(qb + NB -1,qb)

    probability = numMacrostates/np.sum(numMacrostates)

    return numMacrostates, probability


if __name__=="__main__":
    print((numberOfMacroStates(2,2,6)[0]))
