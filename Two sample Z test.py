#H0 : mean of two group is 0
#H1 : mean of two group is not 0

import pandas as pd
from statsmodels.stats import weightstats as stests
df = pd.read_csv("blood_pressure.csv")
print(df[['bp_before','bp_after']].describe())
ztest,pval=stests.ztest(df['bp_before'],x2=df['bp_after'],value=0,alternative= 'two-sided')
print("pval:",float(pval))
if pval< 0.05:
    print("we reject null hypothesis")
else:
    print("we fail to reject null hypothesis")
