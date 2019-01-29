""""""
"""
Suppose you want to know the average height of an oak tree in your local park. On Monday, you measure 10 trees and 
get an average height of 32 ft. On Tuesday, you measure 12 different trees and reach an average height of 35 ft. 
On Wednesday, you measure the remaining 11 trees in the park, whose average height is 31 ft. 
Overall, the average height for all trees in your local park is 32.8 ft.

The individual measurements on Monday, Tuesday, and Wednesday are called samples. 
A sample is a subset of the entire population. The mean of each sample is the sample mean and 
it is an estimate of the population mean.

Note that the sample means (32 ft., 35 ft., and 31 ft.) were all close to the population mean (32.8 ft.), 
but were all slightly different from the population mean and from each other.

For a population, the mean is a constant value no matter how many times it's recalculated. 
But with a set of samples, the mean will depend on exactly what samples we happened to choose. 
From a sample mean, we can then extrapolate the mean of the population as a whole. 
There are many reasons we might use sampling, such as:

We don't have data for the whole population.
We have the whole population data, but it is so large that it is infeasible to analyze.
We can provide meaningful answers to questions faster with sampling.
When we have a numerical dataset and want to know the average value, we calculate the mean. 
For a population, the mean is a constant value no matter how many times it's recalculated. 
But with a set of samples, the mean will depend on exactly what samples we happened to choose. 
From a sample mean, we can then extrapolate the mean of the population as a whole.
"""

import numpy as np

population = np.random.normal(loc=65, scale=3.5, size=300)
population_mean = np.mean(population)

print ("Population Mean: {}".format(population_mean))

sample_1 = np.random.choice(population, size=30, replace=False)
sample_2 = np.random.choice(population, size=30, replace=False)
sample_3 = np.random.choice(population, size=30, replace=False)
sample_4 = np.random.choice(population, size=30, replace=False)
sample_5 = np.random.choice(population, size=30, replace=False)

sample_1_mean = np.mean(sample_1)
print ("Sample 1 Mean: {}".format(sample_1_mean))

sample_2_mean = np.mean(sample_2)
sample_3_mean = np.mean(sample_3)
sample_4_mean = np.mean(sample_4)
sample_5_mean = np.mean(sample_5)

print ("Sample 2 Mean: {}".format(sample_2_mean))
print ("Sample 3 Mean: {}".format(sample_3_mean))
print ("Sample 4 Mean: {}".format(sample_4_mean))
print ("Sample 5 Mean: {}".format(sample_5_mean))


