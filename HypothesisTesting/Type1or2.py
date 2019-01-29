""""""
"""
STATISTICAL CONCEPTS
Type I Or Type II
When we rely on automated processes to make our decisions for us, we need to be aware of how this automation can lead 
to mistakes. Computer programs are as fallible as the humans who design them. As humans capable of programming, 
the responsibility is on us to understand what can go wrong and what we can do to contain these foreseeable problems.

In statistical hypothesis testing, we concern ourselves primarily with two types of error. 
The first kind of error, known as a Type I error, is finding a correlation between things that are not related. 
This error is sometimes called a "false positive" and occurs when the null hypothesis is rejected even though it is true

For example, let's say you conduct an A/B test for an online store and conclude that interface B is significantly 
better than interface A at directing traffic to a checkout page. You have rejected the null hypothesis that 
there is no difference between the two interfaces. If, in reality, your results were due to the groups you happened to 
pick, and there is actually no significant difference between interface A and interface B in the greater population, 
you have been the victim of a false positive.

The second kind of error, a Type II error, is failing to find a correlation between things that are actually related. 
This error is referred to as a "false negative" and occurs when the null hypothesis is accepted even though it is false.

For example, with the A/B test situation, let's say that after the test, you concluded that there was no significant 
difference between interface A and interface B. If there actually is a difference in the population as a whole, 
your test has resulted in a false negative.
"""


import numpy as np

def intersect(list1, list2):
  return [sample for sample in list1 if sample in list2]

# the true positives and negatives:
actual_positive = [2, 5, 6, 7, 8, 10, 18, 21, 24, 25, 29, 30, 32, 33, 38, 39, 42, 44, 45, 47]
actual_negative = [1, 3, 4, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 22, 23, 26, 27, 28, 31, 34, 35, 36, 37, 40, 41, 43, 46, 48, 49]

# the positives and negatives we determine by running the experiment:
experimental_positive = [2, 4, 5, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18, 19, 20, 21, 22, 24, 26, 27, 28, 32, 35, 36, 38, 39, 40, 45, 46, 49]
experimental_negative = [1, 3, 6, 12, 14, 23, 25, 29, 30, 31, 33, 34, 37, 41, 42, 43, 44, 47, 48]

#define type_i_errors and type_ii_errors here
type_i_errors = intersect(experimental_positive, actual_negative)
type_ii_errors = intersect(experimental_negative, actual_positive)

print(type_i_errors)
print(type_ii_errors)

