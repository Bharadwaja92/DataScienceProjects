""""""
"""
As we saw in the previous exercises, while it's possible to plot multiple histograms, it is not a great option for 
comparing distributions. 

Seaborn gives us another option for comparing distributions - a violin plot. 
Violin plots provide more information than box plots because instead of mapping each individual data point, 
we get an estimation of the dataset thanks to the KDE.

Violin plots are less familiar and trickier to read, so let's break down the different parts:

There are two KDE plots that are symmetrical along the center line.
A white dot represents the median.
The thick black line in the center of each violin represents the interquartile range.
The lines that extend from the center are the confidence intervals - just as we saw on the bar plots, 
a violin plot also displays the 95% confidence interval.
"""

"""
Violin Plots are a powerful graphing tool that allows you to compare multiple distributions at once.

Let's look at how our original three data sets look like as violin plots:

sns.violinplot(data=df, x="label", y="value")
plt.show()
"""