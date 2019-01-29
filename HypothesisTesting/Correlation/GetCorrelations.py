import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

pd.set_option('display.max_colwidth', -1)
pd.set_option('float_format', '{:f}'.format)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
np.set_printoptions(threshold=np.nan)

path = 'http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'

mpg_data = pd.read_csv(path, delim_whitespace=True, header=None, na_values='?',
                       names=['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration',
                            'model_year', 'origin', 'name'])

# print(mpg_data.info(verbose=2))
# print(mpg_data[mpg_data['horsepower'].isna()].shape)

corr1 = mpg_data['mpg'].corr(mpg_data['weight'])
print('Correlation between mpg and weight is', corr1)
"""
-0.8317409332443352   implies They are very highly negatively correlated
        As weight goes up, mpg goes down
"""

print('Pairwise correlation')
corr2 = mpg_data.drop(['model_year', 'origin'], axis=1).corr(method='spearman')
print(corr2)

# x = mpg_data.drop(['model_year', 'origin'], axis=1).corr(method='pearson').style.format("{:.2}").background_gradient(cmap=plt.get_cmap('coolwarm'), axis=1)
# w = pd.ExcelWriter('Corr.xlsx')
# x.to_excel(w, 'S1')
# w.save()

print('Plotting correlated values')
plt.rcParams['figure.figsize'] = [16, 6]
fig, ax = plt.subplots(nrows=1, ncols=3)
ax = ax.flatten()

cols = ['weight', 'horsepower', 'acceleration']
colors=['#415952', '#f35134', '#243AB5', '#243AB5']
j=0

for i in ax:
    if j == 0:
        i.set_ylabel('MPG')
    i.scatter(mpg_data[cols[j]], mpg_data['mpg'],  alpha=0.5, color=colors[j])
    i.set_xlabel(cols[j])
    i.set_title('Pearson: %s' % mpg_data.corr().loc[cols[j]]['mpg'].round(2) + ' Spearman: %s' %
                mpg_data.corr(method='spearman').loc[cols[j]]['mpg'].round(2))
    j += 1

plt.show()

print('Done')

