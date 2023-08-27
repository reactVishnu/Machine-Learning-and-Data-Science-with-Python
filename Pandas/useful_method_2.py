import pandas as pd
import numpy as np

df = pd.read_csv('/Users/vishnu.tiwari/Desktop/Python/Machine Learning and Data Science/UNZIP_FOR_NOTEBOOKS_FINAL/'
                 '03-Pandas/'
                 'tips.csv')

# print(df.head())

# print(df.describe().transpose())
# print(df.sort_values('tip', ascending=False).head())


print(df['total_bill'].idxmax())
print(df['total_bill'].idxmin())
print(df.iloc[0])
print(df['tip'])
series = pd.Series(list(df['sex'].value_counts()), ['F', 'M'])
print(series)
# print(df['day'].unique())
# print(df['sex'].replace(['Female', 'Male'], ['F', 'M']))
# print(df['sex'].replace(['Female', 'Male'], ['F', 'M']))
