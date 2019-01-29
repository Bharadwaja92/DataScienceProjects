
from collections import Counter

words = ['also', 'known', 'as', 'a', 'smartbots', 'talkbot', 'a', 'smartbots', ',', 'talkbot','smartbots', 'smartbots']

cn = Counter(words)

print(cn['a'])

import matplotlib.pyplot as plt


x = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
y = [10, 43, 54, 76, 50, 42, 40, 39]

plt.plot(x, y)
plt.show()

plt.semilogx(x, y)
plt.show()
