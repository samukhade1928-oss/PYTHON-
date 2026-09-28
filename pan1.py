#pandas

import pandas as pd #pd is alies
import  numpy as np
ls= ['s' , 'h' , 'a' , 'i' , 'k' , 'h']
data = np.array(ls)
s = pd.Series(data)
print("Series")
print(s)