""""""
"""
HYPOTHESIS TESTING
Assumptions of Numerical Hypothesis Tests
Before we use numerical hypothesis tests, we need to be sure that the following things are true:

1. The samples should each be normally distributed...ish
Data analysts in the real world often still perform hypothesis on sets that aren't exactly normally distributed. 
What is more important is to recognize if there is some reason to believe that a normal distribution is especially 
unlikely. If your dataset is definitively not normal, the numerical hypothesis tests won't work as intended.

For example, imagine we have three datasets, each representing a day of traffic data in three different cities. 
Each dataset is independent, as traffic in one city should not impact traffic in another city. 
However, it is unlikely that each dataset is normally distributed. In fact, each dataset probably has two distinct peaks
, one at the morning rush hour and one during the evening rush hour. 

In this scenario, using a numerical hypothesis test would be inappropriate.

2. The population standard deviations of the groups should be equal
For ANOVA and 2-Sample T-Tests, using datasets with standard deviations that are significantly different from each other
 will often obscure the differences in group means.

To check for similarity between the standard deviations, it is normally sufficient to divide the two standard deviations
 and see if the ratio is "close enough" to 1. "Close enough" may differ in different contexts but generally staying 
 within 10% should suffice.

3. The samples must be independent
When comparing two or more datasets, the values in one distribution should not affect the values in another distribution. 
In other words, knowing more about one distribution should not give you any information about any other distribution.

Here are some examples where it would seem the samples are not independent:

the number of goals scored per soccer player before, during, and after undergoing a rigorous training regimen
a group of patients' blood pressure levels before, during, and after the administration of a drug
It is important to understand your datasets before you begin conducting hypothesis tests on it so that you know you are
choosing the right test.
"""

