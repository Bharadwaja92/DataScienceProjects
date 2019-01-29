""""""
"""
Perhaps, this time, you're a tailor of school uniforms at a middle school. You need to know the average height of people
from 10-13 years old in order to know which sizes to make the uniforms. Knowing the best decisions are based on data, 
you set out to do some research at your local middle school.

Organizing with the school, you measure the heights of some students. Their average height is 57.5 inches. 
You know a little about sampling and decide that measuring 30 out of the 300 students gives enough data to assume 57.5 
inches is roughly the average height of everyone at the middle school. You set to work with this dimension and make 
uniforms that fit people of this height, some smaller and some larger.

Unfortunately, when you go about making your uniforms many reports come back saying that they are too small. 
Something must have gone wrong with your decision-making process! You go back to collect the rest of the data: 
you measure the sixth graders one day (56.7, not so bad), the seventh graders after that (59 inches tall on average), 
and the eighth graders the next day (61.7 inches!). Your sample mean was so far off from your population mean. 
How did this happen?

Well, your sample selection was skewed to one direction of the total population. It looks like you must have measured 
more sixth graders than is representative of the whole middle school. 
How do you get an average sample height that looks more like the average population height?

In the previous exercise, we looked at different sets of samples taken from a population and how the mean of each set 
could be different from the population mean. This is a natural consequence of the fact that a set of samples has less 
data than the population to which it belongs. If our sample selection is poor then we will have a sample mean 
seriously skewed from our population mean.

There is one surefire way to mitigate the risk of having a skewed sample mean — take a larger set of samples. 
The sample mean of a larger sample set will more closely approximate the population mean. 
This phenomenon, known as the Central Limit Theorem, states that if we have a large enough sample size, 
all of our sample means will be sufficiently close to the population mean.

Later, we'll learn how to put numeric values on "large enough" and "sufficiently close".

"""

import numpy as np

# Create population and find population mean
population = np.random.normal(loc=65, scale=100, size=3000)
population_mean = np.mean(population)

# Select increasingly larger samples
extra_small_sample = population[:10]
small_sample = population[:50]
medium_sample = population[:100]
large_sample = population[:500]
extra_large_sample = population[:1000]

# Calculate the mean of those samples
extra_small_sample_mean = np.mean(extra_small_sample)
small_sample_mean = np.mean(small_sample)
medium_sample_mean = np.mean(medium_sample)
large_sample_mean = np.mean(large_sample)
extra_large_sample_mean = np.mean(extra_large_sample)

# Print them all out!
print ("Extra Small Sample Mean: {}".format(extra_small_sample_mean))
print ("Small Sample Mean: {}".format(small_sample_mean))
print ("Medium Sample Mean: {}".format(medium_sample_mean))
print ("Large Sample Mean: {}".format(large_sample_mean))
print ("Extra Large Sample Mean: {}".format(extra_large_sample_mean))

print ("\nPopulation Mean: {}".format(population_mean))



