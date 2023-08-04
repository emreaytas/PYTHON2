import pandas as pd
from numpy.random import randn
df = pd.DataFrame(randn(3,3),index=["A","B","C"],columns=["col1","col2","col3"])
print(df)
"""
       col1      col2      col3
A  0.876487  0.291382 -0.860966
B  0.880688 -0.308720 -1.216277
C  1.038345  0.771560  0.560245
"""
df["col4"] = pd.Series(randn(3),index=["A","B","C"]) # bir col belirttik ve bir seri atadık. bu liste vsde olabilirdi. indexlemesi dataframenin indexlemesi ile aynı olmalıdır.
print(df)
"""
       col1      col2      col3      col4
A  0.876487  0.291382 -0.860966 -0.260276
B  0.880688 -0.308720 -1.216277 -0.303827
C  1.038345  0.771560  0.560245  0.116903
"""

df["col5"] = df["col4"] + df["col3"] # böylede yapabiliriz sonuçta bize gelen yeni bir seri seriler kendi aralarında toplanabilir.
df.drop("col5",axis=1,inplace=True) # axis = 1 y koordinati  axis = 0 x koordinatı. inplace True ile ise kalıcı olmasını sağlarız.