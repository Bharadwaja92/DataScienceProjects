from matplotlib import pyplot as plt
"""
When we have multiple axes in the same picture, we call each set of axes a subplot. 
The picture or object that contains all of the subplots is called a figure.

We can create subplots using .subplot().

The command plt.subplot() needs three arguments to be passed into it:

The number of rows of subplots
The number of columns of subplots
The index of the subplot we want to create
For instance, the command plt.subplot(2, 3, 4) would create "Subplot 4" in a 6-subplot figure

Any plt.plot() that comes after plt.subplot() will create a line plot in the specified subplot. 
"""

# Data sets
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]

# First Subplot
plt.subplot(1, 2, 1)
plt.plot(x, y, color='green')
plt.title('First Subplot')

# Second Subplot
x = [11, 21, 13, 41]
y = [4, 8, 4, 3]
plt.subplot(1, 2, 2)
plt.plot(x, y, color='steelblue')
plt.title('Second Subplot')

# Display both subplots
plt.show()


#######

from matplotlib import pyplot as plt

months = range(12)
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]

plt.subplot(1, 3, 1)
plt.plot(months, temperature)

plt.subplot(1, 3, 2)
plt.plot(temperature, flights_to_hawaii)

plt.subplot(1, 3, 3)
plt.plot(temperature, flights_to_hawaii, 'o')

plt.show()


