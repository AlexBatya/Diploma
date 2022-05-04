import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
from close import runSingle
from scipy.interpolate import interp1d, interp2d 
from Data import *

from Ppotr import * # Если хочИшь найти единичное значение Pp([1],[12000])
from Prasp import * # Если хочИшь найти единичное значение Pr([1],[12000])

P_potr = Pp(M_interp,H_interp)
P_rasp = Pr(M_interp,H_interp)

from Expenses import *
q_h = qh(M_interp,H_interp)
q_km = qkm(M_interp,H_interp)

from VerticalSpeed import * 
n_x = nx(M_interp,H_interp)
V_y = Vy(M_interp,H_interp)
