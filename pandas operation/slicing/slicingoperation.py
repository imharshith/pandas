
import pandas as pd
placement={'NO_0F_OFFERS':[567,618,588,561,555], 'ST_ELIGIBLE':[738,780,853,856,812],'ST_PLACED':[422,528,467,468,449]}
df=pd.DataFrame(placement,index=[2014,2015,2016,2017,2018])
print(df)

df.head(3)  #slicing starting 3 rows

df.tail(2)  #slicing last 2 rows
