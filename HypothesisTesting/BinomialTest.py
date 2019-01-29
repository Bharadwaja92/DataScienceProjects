""""""
"""
Let's imagine that we are analyzing the percentage of customers who make a purchase after visiting a website. 
We have a set of 1000 customers from this month, 58 of whom made a purchase. Over the past year, the number of visitors 
per every 1000 who make a purchase hovers consistently at around 72. Thus, our marketing department has set our target 
number of purchases per 1000 visits to be 72. We would like to know if this month's number, 58, is a significant 
difference from that target or a result of natural fluctuations.

How do we begin comparing this, if there's no mean or standard deviation that we can use? The data is divided into two 
discrete categories, "made a purchase" and "did not make a purchase".

So far, we have been working with numerical datasets. The tests we have looked at, the 1- and 2-Sample T-Tests, ANOVA, 
and Tukey's Range test, will not work if we can't find the means of our distributions and compare them.

If we have a dataset where the entries are not numbers, but categories instead, we have to use different methods.

To analyze a dataset like this, with two different possibilities for entries, we can use a Binomial Test. 
A Binomial Test compares a categorical dataset to some expectation.

Examples include:

Comparing the actual percent of emails that were opened to the quarterly goals
Comparing the actual percentage of respondents who gave a certain survey response to the expected survey response
Comparing the actual number of heads from 1000 coin flips of a weighted coin to the expected number of heads
The null hypothesis, in this case, would be that there is no difference between the observed behavior and the expected 
behavior. If we get a p-value of less than 0.05, we can reject that hypothesis and determine that there is a difference 
between the observation and expectation.

SciPy has a function called binom_test, which performs a Binomial Test for you.

binom_test requires three inputs, the number of observed successes, the number of total trials, and an expected 
probability of success. For example, with 1000 coin flips of a fair coin, we would expect a "success rate" 
(the rate of getting heads), to be 0.5, and the number of trials to be 1000. Let's imagine we get 525 heads. 
Is the coin weighted? This function call would look like:

pval = binom_test(525, n=1000, p=0.5)
It returns a p-value, telling us how confident we can be that the sample of values was likely to occur with the 
specified probability. If we get a p-value less than 0.05, we can reject the null hypothesis and say that it is 
likely the coin is actually weighted, and that the probability of getting heads is statistically different than 0.5.
"""

from scipy.stats import binom_test
pval = binom_test(525, n=1000, p=0.5)

print(pval)
