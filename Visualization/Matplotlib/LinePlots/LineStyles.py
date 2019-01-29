from matplotlib import pyplot

"""
We can specify a different color for a line by using the keyword 'color' with either an HTML color name or a HEX code

We can change make a line dotted or dashed using the keyword 'linestyle'.
Dashed: linestyle='--')
Dotted: linestyle=':')
No line: linestyle='')

We can add a marker using the keyword 'marker':
A circle: marker='o')
A square: marker='s')
A star:   marker='*')

"""

from matplotlib import pyplot as plt

time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

plt.plot(time, revenue, color='purple', linestyle='--')

plt.plot(time, costs, color='#82edc9', marker='s')

plt.show()



