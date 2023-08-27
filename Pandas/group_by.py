import numpy as np
import pandas as pd

df = pd.read_csv('/Users/vishnu.tiwari/Desktop/Python/Machine '
                 'Learning and Data Science/UNZIP_FOR_NOTEBOOKS_FINAL/03-Pandas'
                 '/mpg.csv')

# print(df.groupby('model_year').mean())
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# print(df.groupby(['model_year']).mean()['mpg'])
# print(df.groupby('model_year').mean(numeric_only=True)['mpg'])
# print(df)

k = df.groupby(['model_year', 'cylinders']).mean(numeric_only=True)
print(k)
# k = pd.DataFrame(k, columns=['mpg'])

# print(type(k))
# print(k)
# k.index = list(range(1,14))
# print(k.loc[(70,4)])
# print(df.iloc[0])

print(k.xs(key=4, level='cylinders'))
print(k.loc[[(70,4),(80,4)]])
print(k.sort_index(level='model_year', ascending=False))
print(k.agg(['std', 'mean']))
print(k.agg({'mpg': ['mean', 'max'], 'weight': ['min']}))
