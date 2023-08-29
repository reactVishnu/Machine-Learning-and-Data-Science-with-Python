import numpy as np
import pandas as pd

df = pd.read_csv('/Users/vishnu.tiwari/Desktop/Python/Machine '
                 'Learning and Data Science/UNZIP_FOR_NOTEBOOKS_FINAL/03-Pandas'
                 '/example.csv')
print(df)
df.to_csv('new_file.csv')