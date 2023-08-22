import numpy as np
import pandas as pd

print(pd.Series([1, 2], ['first','second']))

j = pd.Series([1, 2], ['first','second'])

print(j['first'])

df2 = pd.read_csv('/Users/vishnu.tiwari/Desktop/Python/Machine Learning and Data Science/UNZIP_FOR_NOTEBOOKS_FINAL/'
                 '03-Pandas/'
                 'tips.csv')

print(df2)