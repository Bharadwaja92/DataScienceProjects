import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

gradebook = pd.read_csv("gradebook.csv")

"""
By default, Seaborn will place error bars on each bar when you use the barplot() function.

By default, Seaborn uses something called a bootstrapped confidence interval. Roughly speaking, this interval means that 
"based on this data, 95% of similar situations would have an outcome within this range".

In our gradebook example, the confidence interval for the assignments means 
"if we gave this assignment to many, many students, we're confident that the mean score on the assignment would be 
within the range represented by the error bar".

The confidence interval is a nice error bar measurement because it is defined for different types of aggregate functions
such as medians and mode, in addition to means.

If you're calculating a mean and would prefer to use standard deviation for your error bars, you can pass in the 
keyword argument ci="sd" to sns.barplot() which will represent one standard deviation. 

"""
sns.barplot(data=gradebook, x="assignment_name", y="grade", ci='sd')

plt.show()
