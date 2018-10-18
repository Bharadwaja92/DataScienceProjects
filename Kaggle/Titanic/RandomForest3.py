import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold, cross_val_score, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

pd.set_option('display.max_colwidth', -1)
pd.set_option('float_format', '{:f}'.format)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
np.set_printoptions(threshold=np.nan)

train = pd.read_csv('/home/saibharadwaj/Downloads/Ast/Kaggle/Titanic/all/train.csv')
test = pd.read_csv('/home/saibharadwaj/Downloads/Ast/Kaggle/Titanic/all/test.csv')
submission = pd.read_csv('/home/saibharadwaj/Downloads/Ast/Kaggle/Titanic/all/gender_submission.csv')

"""
Training data columns
['PassengerId' 'Survived' 'Pclass' 'Name' 'Sex' 'Age' 'SibSp' 'Parch' 'Ticket' 'Fare' 'Cabin' 'Embarked']
"""
# print(train_df.shape)   #(891, 12)
# print(test.shape)    #(418, 11)

"""
# print(train_df.isnull().sum())
Age missing for 177
Cabin missing for 687
Embarked missing for 2
"""
"""
print(test.isnull().sum())
Age missing for 86
Cabin missing for 327
"""

"""
Plot Barcharts for Better understanding of the data
"""


def plotBarchart(feature):
    survived = train[train['Survived'] == 1][feature].value_counts()
    dead = train[train['Survived'] == 0][feature].value_counts()
    featureDf = pd.DataFrame([survived, dead])
    featureDf.index = ['Survived', 'Dead']
    featureDf.plot(kind='bar', stacked=True, figsize=(10, 5))
    plt.show()


# plotBarchart('Sex')       # Women more likely to survive
#
# plotBarchart('Pclass')    # 1st class more likely to survive and 3rd to Die
#
# plotBarchart('SibSp')     # No SibSp - More likely to die
#
# plotBarchart('Parch')     # No Parch - More likely to die

"""
Feature Engineering - 
    Creating new features from existing ones
    Mapping Character variables to Numerical ones
"""

train['Title'] = train['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
test['Title'] = test['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)

train.loc[:, 'Sex'] = [0 if s == 'male' else 1 for s in train['Sex']]
test.loc[:, 'Sex'] = [0 if s == 'male' else 1 for s in test['Sex']]

train.loc[:, 'Title'] = [0 if s == 'Mr' else 1 if s == 'Mrs' else 2 if s == 'Miss' else 3 for s in train['Title']]
test.loc[:, 'Title'] = [0 if s == 'Mr' else 1 if s == 'Mrs' else 2 if s == 'Miss' else 3 for s in test['Title']]

train['Embarked'] = train['Embarked'].fillna('S')  # Most people boarded from S only

train.loc[:, 'Embarked'] = [0 if s == 'S' else 1 if s == 'C' else 2 for s in train['Embarked']]
test.loc[:, 'Embarked'] = [0 if s == 'S' else 1 if s == 'C' else 2 for s in test['Embarked']]

# Missing Ages filled with Median by Title

train['Age'].fillna(train.groupby('Title')['Age'].transform('median'), inplace=True)
test['Age'].fillna(test.groupby('Title')['Age'].transform('median'), inplace=True)

# Missing Fares filled with Median by Pclass
train['Fare'].fillna(train.groupby('Pclass')['Fare'].transform('median'), inplace=True)
test['Fare'].fillna(test.groupby('Pclass')['Fare'].transform('median'), inplace=True)

train['CabinClass'] = train['Cabin'].str[:1]
test['CabinClass'] = test['Cabin'].str[:1]

cabin_mapping = {"A": 0, "B": 0.1, "C": 0.2, "D": 0.3, "E": 0.4, "F": 0.5, "G": 0.6, "T": 0.7}

train['CabinClass'] = train['CabinClass'].map(cabin_mapping)
test['CabinClass'] = test['CabinClass'].map(cabin_mapping)

# Missing Cabins filled with Median by Pclass
train['CabinClass'].fillna(train.groupby('Pclass')['CabinClass'].transform('median'), inplace=True)
test['CabinClass'].fillna(test.groupby('Pclass')['CabinClass'].transform('median'), inplace=True)

# Create a variable 'FamilySize'

train['FamilySize'] = train['SibSp'] + train['Parch'] + 1
test['FamilySize'] = test['SibSp'] + test['Parch'] + 1

# family_mapping = {1: 0, 2: 0.4, 3: 0.8, 4: 1.2, 5: 1.6, 6: 2, 7: 2.4, 8: 2.8, 9: 3.2, 10: 3.6, 11: 4}
family_mapping = {1: 0, 2: 0.1, 3: 0.2, 4: 0.3, 5: 0.4, 6: 0.5, 7: 0.6, 8: 0.7, 9: 0.8, 10: 0.9, 11: 1.0}
train['FamilySize'] = train['FamilySize'].map(family_mapping)
test['FamilySize'] = test['FamilySize'].map(family_mapping)

#  NEW
train.loc[:, 'MaritalStatus'] = [0 if title == 'Miss' or age < 18 else 1 for title, age in
                                 zip(train['Title'], train['Age'])]
test.loc[:, 'MaritalStatus'] = [0 if title == 'Miss' or age < 18 else 1 for title, age in
                                zip(test['Title'], test['Age'])]

fareP25 = train['Fare'].quantile(0.25)
fareP75 = train['Fare'].quantile(0.75)

train.loc[:, 'EconomicStatus1'] = [0 if fare < fareP25 else 1 if fare < fareP75 else 2 for fare in train['Fare']]
test.loc[:, 'EconomicStatus1'] = [0 if fare < fareP25 else 1 if fare < fareP75 else 2 for fare in test['Fare']]

train.loc[:, 'EconomicStatus'] = [0 if es == 0 and fs > 4 else
                                  1 if (es == 0 and fs < 4) or (es == 1 and fs > 4) else
                                  2 if (es == 1 and fs < 4) or (es == 2 and fs > 4) else 3
                                  for es, fs in zip(train['EconomicStatus1'], train['FamilySize'])]

test.loc[:, 'EconomicStatus'] = [0 if es == 0 and fs > 4 else
                                 1 if (es == 0 and fs < 4) or (es == 1 and fs > 4) else
                                 2 if (es == 1 and fs < 4) or (es == 2 and fs > 4) else 3
                                 for es, fs in zip(test['EconomicStatus1'], test['FamilySize'])]  # , 'EconomicStatus1'

# ['PassengerId' 'Survived' 'Pclass' 'Name' 'Sex' 'Age' 'SibSp' 'Parch' 'Ticket' 'Fare' 'Cabin' 'Embarked']

"""
Male 
(Age > 40 and EconomicStatus = 0)  0
(Age < 40 and EconomicStatus = 1) or (Age > 30 and EconomicStatus = 2) 1
(Age < 30 and EconomicStatus = 3) 2
"""

# train_df.loc[:, 'FinStatus'] = [0 if es == 0 and age > 40 else
#                                   1 if (es == 1 and age < 40) or (es == 2 and age > 30) else
#                                   2 if (es == 3 and age < 30) else 3
#                                   for es, age in zip(train_df['EconomicStatus1'], train_df['Age'])]
#
# test.loc[:, 'FinStatus'] = [0 if es == 0 and age > 40 else
#                                   1 if (es == 1 and age < 40) or (es == 2 and age > 30) else
#                                   2 if (es == 3 and age < 30) else 3
#                                   for es, age in zip(test['EconomicStatus1'], test['Age'])]

# END

train.drop(['Name', 'Parch', 'SibSp', 'Ticket', 'Cabin', 'EconomicStatus1'], axis=1, inplace=True)
test.drop(['Name', 'Parch', 'SibSp', 'Ticket', 'Cabin', 'EconomicStatus1'], axis=1, inplace=True)

X = train.drop(['PassengerId', 'Survived'], axis=1)
y = train['Survived']
testPid = test['PassengerId']
test = test.drop(['PassengerId'], axis=1)

print(X.head(20))

# Now Deploy a model

k_fold = KFold(n_splits=10, shuffle=True, random_state=0)

clf = KNeighborsClassifier(n_neighbors=13)

clf = RandomForestClassifier()

score = cross_val_score(clf, X=X, y=y, cv=k_fold, scoring='accuracy')
print('RandomForestClassifier', np.mean(score) * 100)

parameters = {'n_estimators': (10, 11, 12, 13, 14, 15, 16),
              # 1, 2, 3, 4, 5, 6, 7, 8, 9, , 17, 18, 19, 20, 21, 22, 23, 24
              'min_samples_split': (15, 20, 25, 30),  # 5, 10,
              'min_samples_leaf': (2, 3, 4, 5)}  # , 6, 7, 8, 9, 10

rfc = RandomForestClassifier()

clf = GridSearchCV(rfc, parameters, verbose=0)

# clf = RandomForestClassifier(n_estimators=10, min_samples_split=20, min_samples_leaf=10)
clf.fit(X, y)

print('Best parameters are ', clf.best_params_)

predictions = clf.predict(test)

y_subs = submission['Survived']

print('Final Accuracy', accuracy_score(y_subs, predictions) * 100, '%')

mySubmission = pd.DataFrame({
    "PassengerId": testPid,
    "Survived": predictions
})

mySubmission.to_csv('/home/saibharadwaj/Downloads/Ast/Kaggle/Titanic/all/MySubmission3.csv', index=False)
print(submission.head())

print('Done')

"""
Best parameters are  {'min_samples_leaf': 3, 'n_estimators': 30, 'min_samples_split': 15}
Final Accuracy 88.99521531100478 %
"""
