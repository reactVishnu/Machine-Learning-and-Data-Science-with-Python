import numpy as np
import pandas as pd
import os

np.random.seed(101)
my_data = np.random.randint(0, 101, (4, 3))

print(my_data)

my_index = ['CA', 'NY', 'AZ', 'TX']
my_column = ['Jan', 'Feb', 'Mar']
df = pd.DataFrame(my_data)
print(df)
df = pd.DataFrame(my_data, index=my_index, columns=my_column)

print(df)

df = pd.read_csv('/Users/vishnu.tiwari/Desktop/Python/Machine Learning and Data Science/UNZIP_FOR_NOTEBOOKS_FINAL/'
                 '03-Pandas/'
                 'tips.csv')
print(df)
print(df.columns)
print(df.index)
# print(df.head(10))
print(df.info())
print(df.describe().transpose())
# print(df.total_bill)
# print(df[['total_bill', 'price_per_person']])
#
#
df['percentage_tip'] = np.round((df.tip / df.total_bill) * 100)
print(df.drop('percentage_tip', axis=1))
# df = df.drop('percentage_tip', axis=1)
print(df)


# Working with rows
print(df.index)

# print(df.set_index('Payment ID'))
n = np.arange(0,488,2)
df = df.set_index('Payment ID')
print(df)
# print(pd.Series(n))
df = df.reset_index()

print(df.iloc[1])
# print(df.loc[['Sun2251','Sun2959']])

print(df.iloc[0:5])

one_row = df.iloc[0]
one_row.name = 243
series_row = pd.Series([12, 1, 'MALE', 'NO', 'Sun', 'Dinner', 2, 9, 'Vishnu Tiwari', 12322323232332, 3, "PayID"], df.columns, name=244)
print(series_row)
print(df._append(series_row))
print(df._append(one_row))