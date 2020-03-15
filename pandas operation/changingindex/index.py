#changing the index. making one of the column as an index.

import pandas as pd
import numpy as np

print("CSE DEPARTMENT")

df1=pd.DataFrame({'YEAR':[2015,2016,2017,2018], 'CSE_OFFERS':[126,np.nan,184,164], 'CSE_ELIGIBLE':[110,109,142,142], 'CSE_PLACED':[93,100,133,124]})

df1.set_index('YEAR', inplace=True)
print(df1)
