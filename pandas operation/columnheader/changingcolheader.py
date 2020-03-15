#changing column header

import pandas as pd
import numpy as np

print("ISE DEPARTMENT")

df=pd.DataFrame({'YEAR':[2015,2016,2017,2018], 'ISE_OFFERS':[59,np.nan,42,47], 'ISE_ELIGIBLE':[43,49,39,39], 'ISE_PLACED':[43,46,35,33]})
print(df)

dfc=df.rename(columns={'YEAR':'OUTPUT_YEAR'})
print(dfc)
