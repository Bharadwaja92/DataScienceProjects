""""""
"""
1 Sample T-Testing
Let's imagine the fictional business BuyPie, which sends ingredients for pies to your household, 
so that you can make them from scratch. Suppose that a product manager wants the average age of visitors to BuyPie.com 
to be 30. In the past hour, the website had 100 visitors and the average age was 31. Are the visitors too old? 
Or is this just the result of chance and a small sample size?

We can test this using a univariate T-test. A univariate T-test compares a sample mean to a hypothetical population mean. 
It answers the question "What is the probability that the sample came from a distribution with the desired mean?"

When we conduct a hypothesis test, we want to first create a null hypothesis, which is a prediction that there is no 
significant difference. The null hypothesis that this test examines can be phrased as such: 
"The set of samples belongs to a population with the target mean".

The result of the 1 Sample T Test is a p-value, which will tell us whether or not we can reject this null hypothesis. 
Generally, if we receive a p-value of less than 0.05, we can reject the null hypothesis and state that there is a 
significant difference.

SciPy has a function called ttest_1samp, which performs a 1 Sample T-Test for you.

ttest_1samp requires two inputs, a distribution of values and an expected mean:

tstat, pval = ttest_1samp(example_distribution, expected_mean)
print pval
It also returns two outputs: the t-statistic (which we won't cover in this course), and the p-value — telling us how 
confident we can be that the sample of values came from a distribution with the mean specified.
"""

from scipy.stats import ttest_1samp
import numpy as np

ages = np.genfromtxt("ages.csv")

print(ages)

ages_mean = np.mean(ages)

print(ages_mean)

tstat, pval = ttest_1samp(ages, 30)

print(tstat)
print(pval)

"""
In the last exercise, we got a p-value that was much higher than 0.05, so we cannot reject the null hypothesis. 
Does this mean that if we wait for more visitors to BuyPie, the average age would definitely be 30 and not 31? 
Not necessarily. In fact, in this case, we know that the mean of our sample was 31.

P-values give us an idea of how confident we can be in a result. Just because we don’t have enough data to detect a 
difference doesn’t mean that there isn’t one. Generally, the more samples we have, the smaller a difference 
we’ll be able to detect. You can learn more about the exact relationship between the number of samples and 
detectable differences in the Sample Size Determination course.

To gain some intuition on how our confidence levels can change, let's explore some distributions with different 
means and how our p-values from the 1 Sample T-Tests change.
"""

