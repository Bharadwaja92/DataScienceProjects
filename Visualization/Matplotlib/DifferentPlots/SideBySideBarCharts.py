""""""
"""
Some examples of data that side-by-side bars could be useful for include:

the populations of two countries over time
prices for different foods at two different restaurants
enrollments in different classes for males and females


"""

from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 = [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

n = 1 # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = len(sales1) # Number of sets of bars
w = 0.8 # Width of each bar
store1_x = [t*element + w*n for element in range(d)]

plt.bar(store1_x, sales1)

n = 2  # This is our second dataset (out of 2)
t = 2 # Number of datasets
d = len(sales2) # Number of sets of bars
w = 0.8 # Width of each bar
store2_x = [t*element + w*n for element in range(d)]

plt.bar(store2_x, sales2)


plt.show()



