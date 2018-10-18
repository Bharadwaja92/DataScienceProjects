import numpy as np
import pandas as pd
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

pd.set_option('display.max_colwidth', -1)
pd.set_option('float_format', '{:f}'.format)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
np.set_printoptions(threshold=np.nan)

train = pd.read_csv('/home/saibharadwaj/Downloads/Ast/DSP/Titanic/all/train_df.csv')
test = pd.read_csv('/home/saibharadwaj/Downloads/Ast/DSP/Titanic/all/test.csv')
submission = pd.read_csv('/home/saibharadwaj/Downloads/Ast/DSP/Titanic/all/gender_submission.csv')

cols = list(train.columns.values)

train['Age'].fillna(0, inplace=True)
train['Embarked'].fillna('', inplace=True)
train['Fare'].fillna(0, inplace=True)
test['Age'].fillna(0, inplace=True)
test['Embarked'].fillna('', inplace=True)
test['Fare'].fillna(0, inplace=True)

embarkDict = {' ': 0, '': 0, 'S': 1, 'C': 2, 'Q': 3}
train.loc[:, 'Embarked1'] = [embarkDict[s] for s in train['Embarked']]
train.loc[:, 'Gender'] = [1 if s == 'male' else 0 for s in train['Sex']]
test.loc[:, 'Embarked1'] = [embarkDict[s] for s in test['Embarked']]
test.loc[:, 'Gender'] = [1 if s == 'male' else 0 for s in test['Sex']]

cols.remove('Survived')
cols.remove('Name')
cols.remove('Ticket')
cols.remove('Cabin')
cols.remove('Sex')
cols.remove('Embarked')
cols.remove('PassengerId')

cols1 = cols
cols1.append('Gender')
cols1.append('Embarked1')

X = train[cols1]
y = train['Survived']

clf = SGDClassifier(loss='hinge', penalty="l2", max_iter=10)

clf = KNeighborsClassifier(n_neighbors=10, weights='uniform', algorithm='kd_tree', leaf_size=20, p=20,
                           metric='minkowski')

clf = SVC(C=2, kernel='linear', degree=5, max_iter=10, cache_size=200, gamma='auto')

clf.fit(X, y)

t1 = test[cols]

predictions = clf.predict(t1)

# print(predictions)

y_subs = submission['Survived']

# print(y_subs)

print(accuracy_score(y_subs, predictions) * 100, '%')
