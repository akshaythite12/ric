#Ho - Blood pressure has a mean of 156 units

from statsmodels.stats import weightstats as stests
import pandas as pd
from scipy import stats
df = pd.read_csv("blood_pressure.csv")
print(df['bp_before'].describe())
ztest ,pval = stests.ztest(df['bp_before'], x2=None, value=156)
print("pval:",float(pval))
if pval< 0.05:
    print("we reject null hypothesis")
else:
    print("we fail to reject null hypothesis")
