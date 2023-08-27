import numpy as np
import pandas as pd

print(np.nan)
print(pd.NaT)
print(pd.NA)

# dont use ==, instead use is

df = pd.read_csv('/Users/vishnu.tiwari/Desktop/Python/Machine '
                 'Learning and Data Science/UNZIP_FOR_NOTEBOOKS_FINAL/03-Pandas'
                 '/movie_scores.csv')
print(df)
print(df.isnull())
print(df.notnull())

