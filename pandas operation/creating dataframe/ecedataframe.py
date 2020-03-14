#creating ECE dataframe. 

import numpy as np
import pandas as pd
print("ECE DEPARTMENT")
a={'ECE_OFFERS':[125,np.nan,132,150], 'ECE_ELIGIBLE':[127,131,175,175], 'ECE_PLACED':[110,111,125,112]}
df2=pd.DataFrame(a,index=[2015,2016,2017,2018])
print(df2)
