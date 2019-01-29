""""""
"""
Aesthetically pleasing way on line graphs. 
In Matplotlib, we can use plt.fill_between to shade error. This function takes three arguments:

x-values — this works just like the x-values of plt.plot
lower-bound for y-values — sets the bottom of the shared area
upper-bound for y-values — sets the top of the shared area

Generally, we use fill_between to create a shaded error region, and then plot the actual line over it. 
We can set the alpha keyword to a value between 0 and 1 in the fill_between call for transparency so that we can see 
the line underneath.
"""

from matplotlib import pyplot as plt

months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]

#your work here
plt.plot(months, revenue)
ax = plt.subplot(1, 1, 1)
ax.set_xticks(months)
ax.set_xticklabels(month_names)

y_lower = [0.9 * i for i in revenue]
y_upper = [1.1 * i for i in revenue]

plt.fill_between(months, y_lower, y_upper, alpha=0.2)

plt.show()
