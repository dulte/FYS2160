import numpy as np
import matplotlib.pyplot as plt



def Z(T_over_theta, j_limit = 1e7, eps = 1e-10):
    """
    j_limit how many j's we  want to use, and is default 1e7.
    The function stops to sum if the term is smaller than some epsilon eps. 
    This is 1e-10 by default. The j > 2 is the to ensure that
    the break doesn't happen at the very start.
    """
    result = 0
    for j in range(int(j_limit)):
        term = (2*j + 1)*np.exp(-j*(j+1)*1./T_over_theta)
        result += term
        
        if abs(term) < eps and j>2:
            break
    return result
    
    
if __name__=="__main__":
    N = 10000
    T_over_theta = np.linspace(0.00001,15,N)
    partition = np.zeros(N)
    for i,toT in enumerate(T_over_theta):
        partition[i] = Z(toT)
    
    #For k)
    plt.plot(T_over_theta,partition)
    plt.title(r"$Z_r$ for different values of $T/\theta_r$")
    plt.xlabel(r"$T/\theta_r$")
    plt.ylabel(r"$Z_r$")
    plt.show()
    
    #For l)
    plt.plot(T_over_theta,np.abs(T_over_theta-partition))
    plt.title("The difference between the analytical and numerical value.")
    plt.xlabel(r"$T/\theta_r$")
    plt.ylabel(r"$|T/\theta_r-Z_r|$")
    plt.show()
    print("The difference is about ",T_over_theta[-1]-partition[-1])