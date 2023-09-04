import matplotlib.pyplot as plt

import seaborn as sns

import numpy as np

import pandas as pd

np.random.seed(42)
age = np.random.randint(0,100,200)

df = pd.DataFrame(age, columns=['age'])
print(df.head())

# sns.rugplot(x='age', data=df)
# plt.show()

# sns.displot(data=df, bins=5)
# plt.tight_layout()

sns.kdeplot(x=age, data=df)
plt.show()
