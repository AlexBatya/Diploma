import numpy as np 
import sys
import matplotlib.pyplot as plt 
import pandas as pd
from close import runSingle
from scipy.interpolate import interp1d, interp2d 
from Data import *

# Все библиотечки
from Ppotr import * # Если хочИшь найти единичное значение Pp([1],[12000])
from Prasp import * # Если хочИшь найти единичное значение Pr([1],[12000])
from Expenses import *
from VerticalSpeed import * 

M_interp = np.arange(M1[0],M1[-1],0.3)
H_interp = np.arange(H1[0],H1[-1],4000)

# print(H_interp)

