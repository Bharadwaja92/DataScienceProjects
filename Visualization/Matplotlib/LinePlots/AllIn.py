from matplotlib import pyplot as plt

x = [1, 9, 5, 8, 6]
y1 = [15, 8, 32, 41, 25]
y2 = [2, 36, 24, 61, 18]

plt.plot(x, y1, color='pink', marker='o')
plt.plot(x, y2, color='gray', marker='o')

plt.title('Two Lines on One Graph')
plt.xlabel('Amazing X-axis')
plt.ylabel('Incredible Y-axis')

plt.legend(['Line1', 'Line2'], loc=4)

plt.show()

"""
Good job! Feel free to continue playing around in this space. Maybe make some subplots and separate out the lines. 
Maybe practice with zooming in on certain parts of the graph or selecting certain x- or y-ticks to display. 
When you’re ready, run the code one last time and move on.
"""
