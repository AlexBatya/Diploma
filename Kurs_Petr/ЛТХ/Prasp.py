import numpy as np 
from Data import P0, P00, mass, p

def Pr(M,H):
    Pras = []
    for i in range(len(P0(M,H))):
        Pras.append([])
        for j in range(len(P0(M,H[i]))):
            if H[i]>=11000:
                Pras[i].append(np.multiply(P0(M[j],H[i])*mass*9.81*P00,(p(H[i])/22699.9)))
            else: 
                Pras[i].append(P0(M[j],H[i])*mass*9.81*P00)
    return Pras