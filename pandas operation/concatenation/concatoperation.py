#concatenating two dataframes

import numpy as np
import pandas as pd

print("ECE DEPARTMENT")

a={'YEAR':[2015,2016], 'ECE_OFFERS':[125,np.nan], 'ECE_ELIGIBLE':[127,131], 'ECE_PLACED':[110,111]}
b={'YEAR':[2017,2018], 'ECE_OFFERS':[132,150], 'ECE_ELIGIBLE':[175,175], 'ECE_PLACED':[125,112]}

dfa=pd.DataFrame(a, index=[0,1])
dfb=pd.DataFrame(b, index=[2,3])

concat=pd.concat([dfa,dfb])
print(concat)
