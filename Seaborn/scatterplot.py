import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/Users/vishnu.tiwari/Desktop/Python/Machine Learning and Data Science/UNZIP_FOR_NOTEBOOKS_FINAL/'
                 '05-Seaborn/dm_office_sales.csv'
                 )

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
print(df.head())
plt.figure(dpi=200)
# sns.scatterplot(x='salary',y='sales', data=df)
# sns.scatterplot(x='salary',y='sales', data=df, hue='level of education')
# sns.scatterplot(x='salary',y='sales', data=df, hue='level of education',palette='Dark2')
# sns.scatterplot(x='salary',y='sales', data=df, hue='level of education',size='salary')
# sns.scatterplot(x='salary',y='sales', data=df, hue='level of education',s=70)
# sns.scatterplot(x='salary',y='sales', data=df, hue='level of education',s=70,alpha=0.5)
sns.scatterplot(x='salary', y='sales', data=df, style='level of education', s=100)
sns.scatterplot(x='salary', y='sales', data=df, style='level of education', s=100, hue='level of education')
plt.legend(loc='upper left', fontsize=7.8)
# sns.scatterplot(x='salary',y='sales', data=df, hue='level of education',palette='Dark2')
# plt.xla
plt.show()