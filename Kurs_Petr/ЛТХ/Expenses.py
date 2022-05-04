from Data import Ce0
import numpy as np
from Ppotr import V,Pp

def qh(M,H):
    return np.multiply(0.1*Ce0(M,H),Pp(M,H))

def qkm(M,H):
    return np.divide(np.multiply(0.1*Ce0(M,H),Pp(M,H)),3.6*V(M,H))
    