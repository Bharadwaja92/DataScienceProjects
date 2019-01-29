""""""
"""
To display error visually in a bar chart, we often use error bars to show where each bar could be, 
taking errors into account.

Each of the black lines is called an error bar. 
The taller the bar is, the more uncertain we are about the height of the blue bar. 
The horizontal lines at the top and bottom are called caps. They make it easier to read the error bars.
"""

from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.6, 0.9, 0.4, 0, 0.9, 0]

# Plot the bar graph here
plt.bar(range(len(drinks)), ounces_of_milk, yerr=error, capsize=5)

plt.show()