import numpy as np
import matplotlib.pyplot as plt

j = np.arange(0,300)

z = lambda j, theta_over_T: (2*j + 1)*np.exp(-j*(j+1)*theta_over_T)


theta_over_T = [0.0001,10000]

for toT in theta_over_T:
    plt.bar(j,z(j,toT))
    plt.title(r"$z(j)$ for $T/\theta_r$ = {}".format(1./toT))
    plt.ylabel(r"$z(j)$")
    plt.xlabel("j")
    plt.show()




