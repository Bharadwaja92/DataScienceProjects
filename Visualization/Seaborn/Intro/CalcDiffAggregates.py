""""""
"""
If our data has many outliers, we may want to plot the median.
If our data is categorical, we might want to count how many times each category appears (such as in the case of survey responses).
Seaborn is flexible and can calculate any aggregate you want. To do so, you'll need to use the keyword argument 
'estimator', which accepts any function that works on a list.

For example, to calculate the median, you can pass in np.median to the estimator keyword
sns.barplot(data=df, x="x-values", y="y-values", estimator=np.median)

To calculate the number of times a particular value appears in the Response column , we pass in len:
sns.barplot(data=df, x="Patient ID", y="Response", estimator=len)


We can compare both the Gender and Age Range factors at once by using the keyword hue.

sns.barplot(data=df, x="Gender", y="Response", hue="Age Range")
The hue parameter adds a nested categorical variable to the plot.
Notice that we keep the same x-labels, but we now have different color bars representing each Age Range. 

"""


