import numpy as np
import matplotlib.pyplot as plt

T = np.linspace(0.,10,1000)
eps = 1
k = 1

C = lambda T: (eps**2/(k*T**2))*(3*np.exp(eps/(k*T)))/(np.exp(eps/(k*T)) + 3)**2
           
              
plt.plot(T,C(T))
plt.title(r"Heat Capacity for a Diatomic Molecule, with $\epsilon = ${} and k = {}".format(eps,k))
plt.xlabel("Temperature T")
plt.ylabel(r"Heat Capacity $C_V$")
plt.show()