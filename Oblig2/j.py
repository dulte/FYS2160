import numpy as np
import matplotlib.pyplot as plt



def Z(T_over_theta, j_limit = 1e7, eps = 1e-10):
    """
    j_limit how many j's we  want to use, and is default 1e7.
    The function stops to sum if the term is smaller than some epsilon eps. 
    This is 1e-10 by default.
    """
    result = 0
    for j in range(j_limit):
        term = (2*j + 1)*np.exp(-j*(j+1)*1./T_over_theta)
        result += term
        
        if abs(term) < eps:
            break
    return result
    
    
if __name__=="__main__":
    pass