""""""
"""
We can customize the spacing between our subplots to make sure that the figure we create is visible 
and easy to understand. To do this, we use the plt.subplots_adjust() command. 
'subplots_adjust()' has some keyword arguments that can move your plots within the figure:

left — the left-side margin, with a default of 0.125. You can increase this number to make room for a y-axis label
right — the right-side margin, with a default of 0.9. You can increase this to make more room for the figure, 
        or decrease it to make room for a legend
bottom — the bottom margin, with a default of 0.1. You can increase this to make room for tick mark labels or an x-axis label
top — the top margin, with a default of 0.9
wspace — the horizontal space between adjacent subplots, with a default of 0.2
hspace — the vertical space between adjacent subplots, with a default of 0.2
"""

from matplotlib import pyplot as plt

x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]

plt.subplot(2, 1, 1)
plt.plot(x, straight_line)

plt.subplot(2, 2, 3)
plt.plot(x, parabola)

plt.subplot(2, 2, 4)
plt.plot(x, cubic)

plt.subplots_adjust(wspace=0.35, bottom=0.2)
plt.show()



