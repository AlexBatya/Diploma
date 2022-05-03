import numpy as np
from mainLTX import A,Cx0,a,p,mass,S

def Pp(M,H):
    q =0.7*np.multiply(np.multiply(M,M),np.transpose(p(H)))
    Cy_GP = mass*9.81/(q*S)
    return q

