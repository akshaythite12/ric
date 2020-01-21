#H0: Mean age of given sample is 30.
#H1: Mean age of given sample is not 30
#pip3 install scipy
#pip3 install numpy
from scipy.stats import ttest_1samp
import numpy as np
ages = np.genfromtxt('ages.csv')
print(ages)
ages_mean = np.mean(ages)
print("Mean age:",ages_mean)
print("Test 1: m=30")
tset, pval = ttest_1samp(ages, 30)
print('p-values - ',pval)
if pval< 0.05:
    print("we reject null hypothesis")
else:
    print("we fail to reject null hypothesis")
