import numpy as np
from Data import A,Cx0,p,mass,S

def q(M,H):
    return 0.7*np.multiply(np.multiply(M,M),np.transpose(p(H)))

def Cy(M,H):
    return np.divide(mass*9.81,(q(M,H)*S))

def Cx(M,H):
    return Cx0(M) + np.multiply(A(M),np.multiply(Cy(M,H),Cy(M,H))) 

def K(M,H):
    return np.divide(Cy(M,H),Cx(M,H))

def Pp(M,H):
    return np.divide(mass*9.81,K(M,H))

