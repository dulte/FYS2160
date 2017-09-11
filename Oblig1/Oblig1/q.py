# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 16:07:13 2017

@author: dulte
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial
import seaborn

M = 50000
N = 60

randomstates = np.random.randint(0,2,(M,N))

microstates = np.where(randomstates==0, -1,randomstates)

energies = -(np.sum(microstates == 1,axis=1) - np.sum(microstates == -1,axis=1))/2.
            
            
def exact(N,s,O_max):
    return O_max*np.exp(-2*s**2/float(N))


omega_max = (factorial(N)/(factorial(N/2.))**2)*(M/2**N)
s = np.linspace(-30,30,100)


plt.hist(energies,33)
plt.plot(s,exact(N,s,omega_max),label="Analytical")
plt.title(r"Multiplisity $\Omega$ " + "for M = %g, N = %g" %(M,N))
plt.xlabel(r"Energy $[\mu B]$")
plt.ylabel(r"Multiplisity $\Omega$")
plt.legend()
plt.show()