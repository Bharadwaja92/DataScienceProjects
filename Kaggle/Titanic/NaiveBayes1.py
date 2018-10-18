import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold, cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

pd.set_option('display.max_colwidth', -1)
pd.set_option('float_format', '{:f}'.format)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
np.set_printoptions(threshold=np.nan)

train = pd.read_csv('/home/saibharadwaj/Downloads/Ast/DSP/Titanic/all/train_df.csv')
test = pd.read_csv('/home/saibharadwaj/Downloads/Ast/DSP/Titanic/all/test.csv')
submission = pd.read_csv('/home/saibharadwaj/Downloads/Ast/DSP/Titanic/all/gender_submission.csv')

"""
Training data columns
['PassengerId' 'Survived' 'Pclass' 'Name' 'Sex' 'Age' 'SibSp' 'Parch'
 'Ticket' 'Fare' 'Cabin' 'Embarked']
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


"""
plotBarchart('Sex')       # Women more likely to survive

plotBarchart('Pclass')    # 1st class more likely to survive and 3rd to Die

plotBarchart('SibSp')     # No SibSp - More likely to die

plotBarchart('Parch')     # No Parch - More likely to die
"""

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

train['Cabin'] = train['Cabin'].str[:1]
test['Cabin'] = test['Cabin'].str[:1]

# train_df['Cabin'] = [0 if c =='A' else 0.4 if c =='B' else 0.8 if c =='C' else 1.2 if c =='D' else 1.6 if c =='E'
#                     else 2 if c =='F' else 2.4 if c =='G' else 2.8 for c in train_df['Cabin']]

cabin_mapping = {"A": 0, "B": 0.4, "C": 0.8, "D": 1.2, "E": 1.6, "F": 2, "G": 2.4, "T": 2.8}
cabin_mapping = {"A": 0, "B": 0.1, "C": 0.2, "D": 0.3, "E": 0.4, "F": 0.5, "G": 0.6, "T": 0.7}
train['Cabin'] = train['Cabin'].map(cabin_mapping)
test['Cabin'] = test['Cabin'].map(cabin_mapping)

# Missing Cabins filled with Median by Pclass
train['Cabin'].fillna(train.groupby('Pclass')['Cabin'].transform('median'), inplace=True)
test['Cabin'].fillna(test.groupby('Pclass')['Cabin'].transform('median'), inplace=True)

# Create a variable 'FamilySize'

train['FamilySize'] = train['SibSp'] + train['Parch'] + 1
test['FamilySize'] = test['SibSp'] + test['Parch'] + 1

family_mapping = {1: 0, 2: 0.4, 3: 0.8, 4: 1.2, 5: 1.6, 6: 2, 7: 2.4, 8: 2.8, 9: 3.2, 10: 3.6, 11: 4}
family_mapping = {1: 0, 2: 0.1, 3: 0.2, 4: 0.3, 5: 0.4, 6: 0.5, 7: 0.6, 8: 0.7, 9: 0.8, 10: 0.9, 11: 1.0}
train['FamilySize'] = train['FamilySize'].map(family_mapping)
test['FamilySize'] = test['FamilySize'].map(family_mapping)

train.drop(['Name', 'Parch', 'SibSp', 'Ticket'], axis=1, inplace=True)
test.drop(['Name', 'Parch', 'SibSp', 'Ticket'], axis=1, inplace=True)

# Now Deploy a model

X = train.drop(['PassengerId', 'Survived'], axis=1)
y = train['Survived']
testPid = test['PassengerId']
test = test.drop(['PassengerId'], axis=1)

print(X.head(20))

k_fold = KFold(n_splits=20, shuffle=True, random_state=0)

clf = KNeighborsClassifier(n_neighbors=13)

clf = GaussianNB()

score = cross_val_score(clf, X=X, y=y, cv=k_fold, scoring='accuracy')
print('GaussianNB', np.mean(score) * 100)

"""
RandomForestClassifier  is performing better
"""

clf = RandomForestClassifier()
clf.fit(X, y)

predictions = clf.predict(test)

y_subs = submission['Survived']

print('Final Accuracy', accuracy_score(y_subs, predictions) * 100, '%')

mySubmission = pd.DataFrame({
    "PassengerId": testPid,
    "Survived": predictions
})

# mySubmission.to_csv('/home/saibharadwaj/Downloads/Ast/DSP/Titanic/all/MySubmission1.csv', index=False)
# print(submission.head())

print('Done')
