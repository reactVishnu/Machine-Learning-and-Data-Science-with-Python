import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

fandango = pd.read_csv('/Users/vishnu.tiwari/Desktop/Python/Machine Learning and Data '
                       'Science/UNZIP_FOR_NOTEBOOKS_FINAL/'
                       '06-Capstone-Project/fandango_scrape.csv')

print(fandango.head())
# plt.figure()
# sns.scatterplot(data=fandango, y='VOTES', x='RATING')
# plt.show()
print(fandango.corr(numeric_only=True))
fandango['YEAR'] = fandango['FILM'].str.split('(').str[-1].str.replace(')', '')
# fandango.YEAR.dtypes = 'int'
fandango = fandango.astype({'YEAR': int,})
print(fandango.YEAR.info())

