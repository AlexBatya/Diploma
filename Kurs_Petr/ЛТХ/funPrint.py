import pandas as pd 
import numpy as np

def columnTable(A):
    column_format = ''
    [n,m] = A.shape
    for i in range(m):
        column_format =column_format+'c|'
    return column_format



def LatexTable(table,fileNaame,label,caption,num):
    with open(f'{fileNaame}.tex', "w") as f:
        f.write(
            table
            .rename(columns= {'1':r'$ \omega_z$'})
            .round(num)
            .to_latex(
                caption = caption,
                label = label,
                column_format='|' + columnTable(table),
                escape=False,
                position="H"
            )
        )
