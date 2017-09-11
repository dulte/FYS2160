import numpy as np
import matplotlib.pyplot as plt

M = 50000
N = 60
randomstates = np.random.randint(0,2,(M,N))


microstates = np.where(randomstates==0, -1,1)


energies = np.sum(microstates,axis=1)



plt.hist(energies,33)
plt.show()