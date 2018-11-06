"""
Kaggle:     https://www.kaggle.com/uciml/iris
"""

import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold, cross_val_score, GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

pd.set_option('display.max_colwidth', -1)
pd.set_option('float_format', '{:f}'.format)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
np.set_printoptions(threshold=np.nan)
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=DeprecationWarning)

irisData = pd.read_csv('/home/saibharadwaj/Downloads/Ast/Kaggle/IRIS/Iris.csv', delimiter=',')

cols = list(irisData.columns.values)

print(cols)
print(irisData.shape)

# print(irisData.describe())

irisData.loc[:, 'class'] = [0 if s == 'Iris-versicolor' else 1 if s == 'Iris-virginica' else 3 for s in
                            irisData['Species']]

train, test = train_test_split(irisData, test_size=0.33, random_state=42)

print(train['Species'].value_counts())

# Plot Charts
plt.title('Species histogram')

# pd.value_counts(train['Species']).plot.bar()
# plt.show()

print('Univariate Analysis')

reqdCols = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']

for v in reqdCols:
    print('v is', v)
    plt.title('Univariate Analysis of ' + str(v))
    sns.distplot(train[v], kde=True, bins=40)
    plt.show()

print('Bivariate Analysis')

for v in reqdCols:
    plt.title('Bivariate Analysis of Species vs ' + str(v))
    sns.boxplot(train['Species'], train[v], data=train, palette='OrRd')
    plt.show()

print('Print Heatmap')
sns.heatmap(train.corr(), cmap="OrRd", linecolor='white', linewidths=1)
plt.show()

models = list()

models.append(('LogR', LogisticRegression()))
models.append(('knn', KNeighborsClassifier()))
models.append(('svm', SVC()))
models.append(('NB', GaussianNB()))
models.append(('DTC', DecisionTreeClassifier()))

X = train[reqdCols]
y = train['class']
y = pd.to_numeric(y)  # Not required here
testData = test[reqdCols]
y_actual = test['class']

accs = []

for name, model in models:
    print('Evaluating', name)
    kfold = KFold(n_splits=10, random_state=7)
    acc = cross_val_score(model, X, y, cv=kfold, scoring='accuracy')
    accs.append((name, acc))

for a in accs:
    print(a[0], '->', a[1].mean() * 100, a[1].std())

print('\nTest Logistic Regression')
logreg = LogisticRegression()
logregParameters = {"C": (0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 2, 2.5, 3, 4, 5, 6, 7, 8, 9, 10)}
clf = GridSearchCV(logreg, logregParameters)
clf.fit(X, y)
print('Best parameters are ', clf.best_params_)
best_c = clf.best_params_['C']
clf = LogisticRegression(C=best_c)
clf.fit(X, y)
predictions = clf.predict(testData)
logregAcc = accuracy_score(test['class'], predictions) * 100
print('logregAcc is', logregAcc)

print('\nTest SVM Poly')
svcPoly = SVC(kernel="poly")
svcParameters = {"C": (0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 2, 2.5, 3, 4, 5, 6, 7, 8, 9, 10)}
clf = GridSearchCV(svcPoly, svcParameters)
clf.fit(X, y)
svcPoly = SVC(kernel='poly', C=clf.best_params_['C'])
svcPoly.fit(X, y)
predictions = clf.predict(testData)
svcPolyAcc = accuracy_score(test['class'], predictions) * 100
print('svcPolyAcc is', svcPolyAcc)

print('\nTest SVM rbf')
svcrbf = SVC(kernel="rbf")
svcParameters = {"C": (0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 2, 2.5, 3, 4, 5, 6, 7, 8, 9, 10)}
clf = GridSearchCV(svcrbf, svcParameters)
clf.fit(X, y)
# print('Best params are ', clf.best_params_)
# print('clf is ', clf)
svcrbf = SVC(kernel='rbf', C=clf.best_params_['C'])
svcrbf.fit(X, y)
predictions = clf.predict(testData)
svcrbfAcc = accuracy_score(test['class'], predictions) * 100
print('svcrbfAcc is', svcrbfAcc)

print('Done')

"""
LogR -> 95.0 0.04999999999999999
knn -> 94.0 0.06633249580710798
svm -> 95.0 0.06708203932499368
NB -> 94.0 0.07999999999999999
DTC -> 90.0 0.09999999999999999
"""
