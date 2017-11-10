# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
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
# Oppgave i) #
##############

T = np.array([100,110,115,120,125])
V = np.linspace(0.4,6,1000,endpoint=True)*0.089
Y = np.array([11,19,23,27.5,32.53])

diff = np.zeros_like(Y)

for i,t in enumerate(T):
    plt.plot(V,P_VT(V,t),label=r"$T$=%g K" %t)
    plt.plot(V,np.ones(len(V))*Y[i], label="Seperation of equal area")
    plt.title(r"Equal Areal for T = %g" %t)
    plt.ylabel(r"$P [atm]$")
    plt.xlabel(r"$V [l/mol]$")
    plt.legend()
    plt.show()
    intersections = V[argrelextrema(np.abs(Y[i]-P_VT(V,t)),np.less)]
    diff[i] = intersections[-1]-intersections[0] 
    print("For T = {}: V_L = {}, V_g = {}, V_g - V_L = {}".format(t,\
                  intersections[0],intersections[-1],\
                  intersections[-1]-intersections[0]))

slope, intercept, r_value, p_value, std_err = stats.linregress(T,diff)
T_cont = np.linspace(T[0],T[-1],100)
plt.plot(T,diff,".")
plt.plot(T_cont, slope*T_cont + intercept)
plt.title(r"$V_g - V_L$ as teperature increases")
plt.xlabel("Temperature [K]")
plt.ylabel(r"$V_g - V_L$")
plt.legend()
plt.show()

print("V_g - V_L = {}*T + {}".format(slope,intercept))

print("T_c = {}".format(-intercept/slope))





        
        
        
    
    

