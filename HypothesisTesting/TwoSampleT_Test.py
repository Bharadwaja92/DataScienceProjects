""""""
"""
2 Sample T-Test
Suppose that last week, the average amount of time spent per visitor to a website was 25 minutes. 
This week, the average amount of time spent per visitor to a website was 28 minutes. 
Did the average time spent per visitor change? Or is this part of natural fluctuations?

One way of testing whether this difference is significant is by using a 2 Sample T-Test. 
A 2 Sample T-Test compares two sets of data, which are both approximately normally distributed.

The null hypothesis, in this case, is that the two distributions have the same mean.

We can use SciPy's ttest_ind function to perform a 2 Sample T-Test. It takes the two distributions as inputs and 
returns the t-statistic (which we don't use), and a p-value. 
"""

from scipy.stats import ttest_ind

t, p = ttest_ind()