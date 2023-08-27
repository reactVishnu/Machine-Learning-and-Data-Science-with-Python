import numpy as np
import pandas as pd

df = pd.read_csv('/Users/vishnu.tiwari/Desktop/Python/Machine Learning and Data Science/UNZIP_FOR_NOTEBOOKS_FINAL/'
                 '03-Pandas/'
                 'tips.csv')

print(df.head())


def app_changer(some):
    return some * 2


df['double_tip'] = df['tip'].apply(app_changer)
print(df['double_tip'].head())


# For multiple column

def Quality(total_bill, tip):
    if tip / total_bill > 0.25:
        return "Generous"
    else:
        return 'Other'


df['Quality'] = df[['total_bill', 'tip']].apply(lambda x: Quality(x['total_bill'], x['tip']), axis=1)
print(df['Quality'])
df['Quality'] = np.vectorize(Quality)(df['total_bill'], df['tip'])
print(df.head())
