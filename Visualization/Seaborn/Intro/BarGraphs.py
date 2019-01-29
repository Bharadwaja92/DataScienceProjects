import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

"""  In Matplotlib  """

df = pd.read_csv("results.csv")
# print(df)
print(df.columns.values)
print(df.head())
# import sys
# sys.exit(2)
ax = plt.subplot()
plt.bar(range(len(df)),
        df["Mean Satisfaction"])
ax.set_xticks(range(len(df)))
ax.set_xticklabels(df.Gender)
plt.xlabel("Gender")
plt.ylabel("Mean Satisfaction")

plt.show()

"""   In Seaborn   
With Seaborn, you can use the sns.barplot() command to do the same thing.

The Seaborn function sns.barplot(), takes at least three keyword arguments:

data: a Pandas DataFrame that contains the data (in this example, data=df)
x: a string that tells Seaborn which column in the DataFrame contains otheur x-labels (in this case, x="Gender")
y: a string that tells Seaborn which column in the DataFrame contains the heights we want to plot for each bar 
(in this case y="Mean Satisfaction")
By default, Seaborn will aggregate and plot the mean of each category.
"""

print(df)

sns.barplot(
	data= df,
	x= 'Gender',
	y= 'Mean Satisfaction'
)

plt.show()


