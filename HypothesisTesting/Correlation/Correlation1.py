import numpy as np
import pandas as pd
from pandas import plotting
import matplotlib.pyplot as plt

"""
Correlation values range between -1 and 1
"""

np.random.seed(1)

x = np.random.randint(0, 50, 1000)          # 1000 random integers between 0 and 50

y = x + np.random.randint(0, 10, 1000)      # Positive correlation with Noise
print(np.corrcoef(x, y))
plt.title('Positive correlation')
plt.scatter(x, y)
# plt.show()

y = 100- x - np.random.randint(0, 10, 1000)      # Negative correlation with Noise
print(np.corrcoef(x, y))
plt.title('Negative correlation')
plt.scatter(x, y)
# plt.show()

y = np.random.randint(0, 50, 1000)      # No/Weak correlation
print(np.corrcoef(x, y))
plt.title('Negative correlation')
plt.scatter(x, y)
plt.show()

print('\nPANDAS DATAFRAME')

df = pd.DataFrame({'a': np.random.randint(0, 50, 1000)})
df['b'] = df['a'] + np.random.normal(0, 10, 1000) # positively correlated with 'a'
df['c'] = 100 - df['a'] + np.random.normal(0, 5, 1000) # negatively correlated with 'a'
df['d'] = np.random.randint(0, 50, 1000) # not correlated with 'a'

print(type(df.corr()))
print(df.corr())

plotting.scatter_matrix(df, figsize=(6, 6))
plt.show()

plt.matshow(df.corr())
plt.xticks(range(len(df.columns)), df.columns)
plt.yticks(range(len(df.columns)), df.columns)
plt.colorbar()
plt.title('Correlation matrix')
plt.show()

