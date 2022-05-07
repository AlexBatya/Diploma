import sys 
import numpy as np 
from Data import P0, P00, mass, p

def Pr(M,H):
    Pras = []
    for i in range(len(P0(M,H))):
        if H[i]>=11000:
            Pras.append(P0(M,H[i])*mass*9.81*P00*(p(H[i])/22699.9))
        else: 
            Pras.append(P0(M,H[i])*mass*9.81*P00)
    return Pras