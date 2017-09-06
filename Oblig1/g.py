import numpy as np
import matplotlib.pyplot as plt
from scipy.special import binom
import seaborn as sns

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
    q = 100
    NA = 30
    NB = 70
    qa = np.arange(q+1)
    prob = numberOfMacroStates(NA,NB,q)[1]

    plt.plot(qa,prob)
    plt.title(r"Probability of $q_A$")
    plt.xlabel(r"$q_A$")
    plt.ylabel(r"$P(q_A)$")
    plt.show()

    mostLikely = np.argmax(prob)
    print "Most probable is %g with probability %g" %(qa[mostLikely],prob[mostLikely])
