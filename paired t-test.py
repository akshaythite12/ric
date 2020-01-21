#H0 - The mean difference between sample 1 and sample 2 is equal to 0.
#H1 - The mean difference between sample 1 and sample 2 is not equal to 0

from scipy import stats 
import matplotlib.pyplot as plt 
import pandas as pd 
df = pd.read_csv("blood_pressure.csv") 
print(df[['bp_before','bp_after']].describe()) 
tst,pval=stats.ttest_rel(df['bp_before'], df['bp_after']) 
if pval< 0.05:  
    print("we reject null hypothesis") 
else: 
    print("we fail to reject null hypothesis") 
