#merging multiple dataframe.

import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.array([
    ['CSE', 126, 110, 93],
    ['ECE', 125, 127, 110],
    ['ISE', 59, 43, 43]]),
    columns=['BRANCH', 'OFFER2015', 'ELIGIBLE2015','PLACED2015'])

df2 = pd.DataFrame(np.array([
    ['CSE', 135, 142, 124],
    ['ECE', 130, 175, 112],
    ['ISE', 51, 39, 33]]),
    columns=['BRANCH', 'OFFER2016', 'ELIGIBLE2016','PLACED2016'])
    
df3 = pd.DataFrame(np.array([
    ['CSE', 184, 142, 133],
    ['ECE', 132, 175, 125],
    ['ISE', 42, 39, 35]]),
    columns=['BRANCH', 'OFFER2017', 'ELIGIBLE2017','PLACED2017'])

df4 = pd.DataFrame(np.array([
    ['CSE', 164, 142, 124],
    ['ECE', 150, 175, 112],
    ['ISE', 47, 39, 33]]),
    columns=['BRANCH', 'OFFER2018', 'ELIGIBLE2018','PLACED2018'])

pd.merge(pd.merge(df1,df2,on='BRANCH'),pd.merge(df3,df4,on='BRANCH'),on='BRANCH')
