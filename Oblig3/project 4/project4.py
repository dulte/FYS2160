import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


def find_CV(name):
	d_data = (np.loadtxt(name,skiprows=1).T)
	dT = d_data[3]
	dQ = d_data[2]

	slope, intercept, r_value, p_value, std_err = stats.linregress(dT,dQ)
	return slope, std_err


##############
# Oppgave d) #
##############


d_data = (np.loadtxt("4dresults.txt",skiprows=1).T)
dT = d_data[3]
dQ = d_data[2]

slope, intercept, r_value, p_value, std_err = stats.linregress(dT,dQ)

dT_cont = np.linspace(np.min(dT),np.max(dT),1000)

plt.plot(dT,dQ,".")
plt.plot(dT_cont,slope*dT_cont + intercept,label="Linear Fit")
plt.title("dT vs dQ and the linear fit for finding $C_V$")
plt.xlabel(r"dT $[\epsilon/k]$")
plt.ylabel(r"dQ $[\epsilon]$")
plt.legend()
plt.show()

print("This gives a C_V of {} +/- {}".format(slope,std_err))


##############
# Oppgave f) #
##############

Ts = [1,0.694,2,6,10,13]
T_names = ["0694","2","6","10","13"]
C_Vs = [slope]
uncertainties = [std_err]

for t,name in zip(Ts[1:],T_names):

	slope,std_err = find_CV("4dresultsT%s.txt" %name)
	
	C_Vs.append(slope)
	uncertainties.append(std_err)

plt.errorbar(Ts,C_Vs,uncertainties,fmt=".-.")
plt.title(r"Heat Capacity $C_V$ as Temperature increases. For $\rho = 0.01$")
plt.xlabel("T")
plt.ylabel(r"$C_V$")
plt.show()


##############
# Oppgave g) #
##############

rhos = [0.01,0.2,0.4,0.6,0.8]
rho_names = ["001","02","04","06","08"]
C_Vs = []
uncertainties = []

for r,name in zip(rhos,rho_names):

	slope,std_err = find_CV("4gresultsRho%s.txt" %name)

	C_Vs.append(slope)
	uncertainties.append(std_err)

plt.errorbar(rhos,C_Vs,uncertainties,fmt=".-.")
plt.title(r"Heat Capacity $C_V$ as $\rho$ increases. For T=2")
plt.xlabel(r"$\rho$")
plt.ylabel(r"$C_V$")
plt.show()

##############
# Oppgave h) #
##############



C_P_diluted = find_CV("4hdiluted.txt")[0]
C_V_diluted = C_Vs[0]

C_P_tp = find_CV("4hTp.txt")[0]
C_V_tp = C_Vs[-1]

print("Diluted: C_V = {}, C_P = {}".format(C_V_diluted,C_P_diluted))
print("Triple point: C_V = {}, C_P = {}".format(C_V_tp,C_P_tp))

print("For the diluted density, C_P - C_V = {}".format(C_P_diluted - C_V_diluted))
print("For the triple point density, C_P - C_V = {}".format(C_P_tp - C_V_tp))


##############
# Oppgave i) #
##############

slope, std_err = find_CV("4i.txt")

print("C_V for N2 = {}".format(slope))


