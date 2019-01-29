""""""
"""
In the last exercise, we saw that the probability of making a Type I error got dangerously high as we performed more t-tests.

When comparing more than two numerical datasets, the best way to preserve a Type I error probability of 0.05 is to 
use ANOVA. ANOVA (Analysis of Variance) tests the null hypothesis that all of the datasets have the same mean. 
If we reject the null hypothesis with ANOVA, we're saying that at least one of the sets has a different mean; 
however, it does not tell us which datasets are different.

We can use the SciPy function f_oneway to perform ANOVA on multiple datasets. It takes in each dataset as a different 
input and returns the t-statistic and the p-value. For example, if we were comparing scores on a videogame between 
math majors, writing majors, and psychology majors, we could run an ANOVA test with this line:

fstat, pval = f_oneway(scores_mathematicians, scores_writers, scores_psychologists)

The null hypothesis, in this case, is that all three populations have the same mean score on this videogame. 
If we reject this null hypothesis (if we get a p-value less than 0.05), we can say that we are reasonably confident 
that a pair of datasets is significantly different. 
After using only ANOVA, we can't make any conclusions on which two populations have a significant difference.
"""

from scipy.stats import ttest_ind
from scipy.stats import f_oneway
import numpy as np

a = np.genfromtxt("store_a.csv",  delimiter=",")
b = np.genfromtxt("store_b.csv",  delimiter=",")
c = np.genfromtxt("store_c.csv",  delimiter=",")

pval = f_oneway(a, b, c).pvalue
print(pval)

b = np.genfromtxt("store_b_new.csv",  delimiter=",")

pval = f_oneway(a, b, c).pvalue
print(pval)






