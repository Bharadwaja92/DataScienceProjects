""""""
"""
In the last exercise, we looked at data where customers visited a website and either made a purchase or did not make 
a purchase. What if we also wanted to track if visitors added any items to their shopping cart? 
With three discrete categories of data per dataset, we can no longer use a Binomial Test. 
If we have two or more categorical datasets that we want to compare, we should use a Chi Square test. 
It is useful in situations like:

An A/B test where half of users were shown a green submit button and the other half were shown a purple submit button.
Was one group more likely to click the submit button?
Men and women were both given a survey asking "Which of the following three products is your favorite?" 
Did the men and women have significantly different preferences?
In SciPy, you can use the function chi2_contingency to perform a Chi Square test.

The input to chi2_contingency is a contingency table where:

The columns are each a different condition, such as men vs. women or Interface A vs. Interface B
The rows represent different outcomes, like "Survey Response A" vs. "Survey Response B" or "Clicked a Link" vs. "Didn't Click"
This table can have as many rows and columns as you need.

In this case, the null hypothesis is that there's no significant difference between the datasets. 
We reject that hypothesis, and state that there is a significant difference between two of the datasets
if we get a p-value less than 0.05.
"""

from scipy.stats import chi2_contingency

# Contingency table
#         harvester |  leaf cutter
# ----+------------------+------------
# 1st gr | 30       |  10
# 2nd gr | 35       |  5
# 3rd gr | 28       |  12

X = [[30, 10],
     [35, 5],
     [28, 12]]
chi2, pval, dof, expected = chi2_contingency(X)
print(pval)

X = [[30, 10],
     [35, 5],
     [28, 12],
     [20, 20]]
chi2, pval, dof, expected = chi2_contingency(X)
print(pval)

