import numpy as np
import matplotlib.pyplot as plt


def numerical_energy(T, theta=1, k=1, j_limit=1e7, eps=1e-10):
    result = 0
    result_z = 0
    for j in range(int(j_limit)):
        term = j*(j+1)*k*theta*(2*j + 1)*np.exp(-j*(j+1)*theta/float(T))
        term_z = (2*j + 1)*np.exp(-j*(j+1)*theta/float(T))
        result += term
        result_z += term_z
        
        if abs(term) < eps and j > 2:
            break
    return result/result_z

def numerical_CV(E,h):
    return 1./(2*h)*(E[2:]-E[:-2])


def approx_energy_high(T,k=1):
    return k*T

def approx_energy_low(T,k=1,theta=1):
    return (6*theta*k)/(np.exp(2*theta/T) + 3.)

def approx_cv_high(T,k=1):
    return k

def approx_cv_low(T,k=1,theta=1):
    return (12*theta**2*k*np.exp(2*theta/T))/(T**2*(np.exp(2*theta/T)+3.)**2)


if __name__=="__main__":
    k = 1
    theta = 1
    T_start = 0.01
    T_end = 15
    T_N = 10000
    dT = (T_end-T_start)/T_N
    T = np.linspace(T_start,T_end,T_N,endpoint=True)
    
    
    #Gets the numerical energies
    num_energies = np.zeros_like(T)
    for i,t in enumerate(T):
        num_energies[i] = numerical_energy(t,j_limit=1e3)
    
    #Gets the numerical heat capacities
    num_cv = numerical_CV(num_energies,dT)
    
    #Get the analytical approximations
    approx_energies_h = approx_energy_high(T)
    approx_energies_l = approx_energy_low(T)
    approx_cvs_l = approx_cv_low(T)
    approx_cvs_h = np.vectorize(approx_cv_high)(T) 
    """
    #The np.vectorize is to ensure that the constant k is returned as an array
    """

    
    #Plots for energies:
    plt.plot(T,num_energies,label="Numerical")
    plt.plot(T,approx_energies_h,label="High T")
    plt.plot(T,approx_energies_l,label="Low T")
    plt.legend()
    plt.title("The numerical and analytical Energies")
    plt.xlabel("T")
    plt.ylabel("Energy")
    plt.show()
 
    #Plots for heat capacities:
    plt.plot(T[1:-1],num_cv,label="Numerical")
    plt.plot(T[1:-1],approx_cvs_h[1:-1],label="High T")
    plt.plot(T[1:-1],approx_cvs_l[1:-1],label="Low T")
    plt.legend()
    plt.title("The numerical and analytical heat capacities")
    plt.xlabel("T")
    plt.ylabel("Heat Capacity")
    plt.show()
 
    
    
    
    
    
    

