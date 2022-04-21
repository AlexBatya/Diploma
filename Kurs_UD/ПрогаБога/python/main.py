import pandas as pd 
# import matplotlib.pyplot as plt
import csv 
import numpy as np

H=pd.read_excel('Data/H.xlsx')
M=pd.read_excel('Data/MAX.xlsx')
M=pd.DataFrame(['gf'],H)

K_wz=pd.read_excel('Data/K_wz.xlsx')
K_v=pd.read_excel('Data/K_v.xlsx')