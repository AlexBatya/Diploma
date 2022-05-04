import numpy as np 
from Data import mass
from Ppotr import Pp, V
from Prasp import Pr

def nx(M,H):
    return (Pr(M,H)-Pp(M,H))/(0.95*mass*9.81)

def Vy(M,H):
    return np.multiply(nx(M,H),V(M,H))