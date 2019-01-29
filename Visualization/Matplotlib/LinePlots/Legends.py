""""""
"""
When we have multiple lines on a single graph we can label them by using the command plt.legend().

The legend method takes a list with the labels to display.
plt.legend() can also take a keyword argument loc, which will position the legend on the figure.

These are the position values loc accepts:

Number Code	String
0	best
1	upper right
2	upper left
3	lower left
4	lower right
5	right
6	center left
7	center right
8	lower center
9	upper center
10	center
"""

from matplotlib import pyplot as plt

months = range(12)
hyrule = [63, 65, 68, 70, 72, 72, 73, 74, 71, 70, 68, 64]
kakariko = [52, 52, 53, 68, 73, 74, 74, 76, 71, 62, 58, 54]
gerudo = [98, 99, 99, 100, 99, 100, 98, 101, 101, 97, 98, 99]

plt.plot(months, hyrule)
plt.plot(months, kakariko)
plt.plot(months, gerudo)

#create your legend here
legend_labels = ['hyrule', 'kakariko', 'gerudo']
plt.legend(legend_labels, loc=8)

plt.show()