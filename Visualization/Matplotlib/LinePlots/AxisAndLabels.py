from matplotlib import pyplot as plt

"""
To zoom, we can use plt.axis(). We use plt.axis() by feeding it a list as input. This list should contain:
The minimum x-value displayed
The maximum x-value displayed
The minimum y-value displayed
The maximum y-value displayed
"""
"""
We can label the x- and y- axes by using plt.xlabel() and plt.ylabel(). 
The plot title can be set by using plt.title().
"""


x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]
plt.plot(x, y)
plt.axis([0, 3, 2, 5])
plt.show()
x = range(12)
y = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]
plt.plot(x, y)
plt.axis([0, 12, 2900, 3100])
plt.show()


