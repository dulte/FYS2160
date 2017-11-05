# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

##############
# Oppgave c) #
##############

P_VT = lambda T,V: 8*T/(3*V-1.)-3./V**2

T = np.array([1.,0.95,.9,.8])
V = np.linspace(0.4,6,1000,endpoint=True)

for t in T:
    plt.plot(V,P_VT(t,V),label=r"$\hat{T}$=%g" %t)

plt.title("Dimensionless Pressure of van der Waals Gas")
plt.ylabel(r"$\hat{P}$")
plt.xlabel(r"$\hat{V}$")
plt.legend()
plt.show()


##############
# Oppgave e) #
##############

P_rhoT = lambda T,rho: 8*T*rho/(3.-rho)-3*rho**2

T = np.array([1.,0.95,.9,.8])
rho = np.linspace(0,2,1000,endpoint=True)

for t in T:
    plt.plot(rho,P_rhoT(t,rho),label=r"$\hat{T}$=%g" %t)

plt.title(r"Dimensionless Pressure as a Function of $\hat{\rho}$ of van der Waals Gas")
plt.ylabel(r"$\hat{P}$")
plt.xlabel(r"$\hat{\rho}$")
plt.legend()
plt.show()

##############
# Oppgave g) #
##############

def k(P,rho):
    drho = rho[1]-rho[0]
    dP_drho = (P[1:]-P[:-1])/drho
    return 1/rho[:-1]*1./dP_drho


for t in T:
    P = P_rhoT(t,rho)
    plt.plot(rho[:-1],k(P,rho),".",label=r"$\hat{T}$=%g" %t)

plt.plot(rho[:-1],np.zeros_like(rho[:-1]),"--")
plt.title("Isothermal compressibility")
plt.legend()
plt.ylim(-5,5)
plt.xlabel(r"$\hat{\rho}$")
plt.ylabel(r"$\kappa$")
plt.show()


##############
# Oppgave h) #
##############

def P_VT(V,T):
    V_c = 0.089
    T_c = 126
    P_c = 33.6
    P = P_c*(8*T/T_c/(3*V/V_c-1.)-3.*V_c**2/V**2)
    return P


T = np.array([77,100,110,115,120,125])
V = np.linspace(0.4,6,1000,endpoint=True)*0.089

for t in T:
    plt.plot(V,P_VT(V,t),label=r"$T$=%g K" %t)

plt.title(r"PV isotherms for $N_2$")
plt.ylabel(r"$P [atm]$")
plt.xlabel(r"$V [l/mol]$")
plt.legend()
plt.show()

##############
# Oppgave j) #
##############

def integrate(P,dV):
    return np.sum(P)*dV

def find_intersect_arg(P):
    abs_P = np.abs(P)
    return argrelextrema(abs_P,np.less)

def find_equal_area(P,V,T,initial_guess,eps=1e-5,iterations=1000,learningRate=0.01,tries=4):
    dV = V[1]- V[0]
    y = initial_guess
    
    for j in range(tries):
        for i in range(int(iterations)):
            arg_min = find_intersect_arg(P(V,T)-y)[0]
            
            if len(arg_min) < 3:
                y -= learningRate
                continue
            under = integrate(P(V[arg_min[0]:arg_min[1]+1],T),dV)
            over = integrate(P(V[arg_min[1]:arg_min[2]+1],T),dV)
            
            error = np.sign(over-under)*(over-under)**2
            y += error*learningRate
            if abs(error) <= eps:
                return V[arg_min[0]],V[arg_min[2]]
        
        if len(arg_min) == 3:
            print("Best approximation with current learning rate and iterations")
            
            return V[arg_min[0]],V[arg_min[2]]
        else:
            learningRate *= 0.1
            y = initial_guess
    print("Could not find 3 intersections in {} tries".format(tries))
    
V = np.linspace(0.4,40,60000,endpoint=True)*0.089
T = np.array([100,110,115,120,125])
init_guess = [25,30,35,40,45]
temperatures = []
for t,i in zip(T,init_guess):
    V_L,V_g = find_equal_area(P_VT,V,t,i,iterations=1e6,learningRate=0.005)
    print(V_L,V_g,V_g-V_L)
    temperatures.append(V_g-V_L)
    
plt.plot(T,temperatures)

plt.title(r"$V_g - V_L$ as temperature goes to $T_c$")
plt.xlabel("Temperature [K]")
plt.ylabel("$V_g - V_L$")
plt.show()
        
        
        
    
    

