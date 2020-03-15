#creating ISE dataframe.

import numpy as np
import pandas as pd

print("ISE DEPARTMENT")
a={'ISE_OFFERS':[59,np.nan,42,47], 'ISE_ELIGIBLE':[43,49,39,39], 'ISE_PLACED':[43,46,35,33]}
df3=pd.DataFrame(a,index=[2015,2016,2017,2018])
print(df3)
