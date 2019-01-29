""""""
"""
Examples:
x-axis — famous buildings        y-axis — heights
x-axis — different planets       y-axis — number of days in the year
x-axis — programming languages   y-axis — lines of code written by you
"""
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales = [91, 76, 56, 66, 52, 27]

plt.bar(range(len(sales)), sales)

"""
For better visualization, 
Set the x-tick positions using a list of numbers
Set the x-tick labels using a list of strings
use the rotation keyword to rotate your labels by a specified number of degrees

If we skip setting the x-ticks before the x-labels, we might end up with labels in the wrong place.
"""

ax = plt.subplot()
ax.set_xticks(range(len(drinks)))
ax.set_xticklabels(drinks)

plt.show()

