# import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('/home/saibharadwaj/Downloads/Ast/Kaggle/WorldCupMatches.csv')

print(df.head())

df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']

print(df.head())

sns.set_style('whitegrid')
sns.set_context('poster')

f, ax = plt.subplots(figsize=(12, 7))

ax = sns.barplot(x='Year', y='Total Goals', data=df)

ax.set_title('No. of Goals per year')

plt.show()

df_goals = pd.read_csv('/home/saibharadwaj/Downloads/Ast/Kaggle/goals.csv')

print(df_goals.head())

sns.set_context(context='notebook', font_scale=1.25)

f, ax2 = plt.subplots(figsize=(12, 7))

ax2 = sns.boxplot(x='year', y='goals', data=df_goals, palette='Spectral')

ax2.set_title('No. of Goals per year2')

plt.show()

