#creating CSE dataframe.

import numpy as np
import pandas as pd
print("CSE DEPARTMENT")
a={'CSE_OFFERS':[126,np.nan,184,164], 'CSE_ELIGIBLE':[110,109,142,142], 'CSE_PLACED':[93,100,133,124]}
df1=pd.DataFrame(a, index=[2015,2016,2017,2018])
print(df1)

#x=df1.dropna(axis=1)  ---this drops the column with NaN values.
#x=df1.dropna(axis=0)  ---this drops the row with NaN values.
#x=df1.dropna()        ---this drops the row with NaN values.
#print(x)
