import pandas as pd

df = pd.read_csv('/Users/vishnu.tiwari/Desktop/Python/Machine '
                 'Learning and Data Science/UNZIP_FOR_NOTEBOOKS_FINAL/03-Pandas'
                 '/hotel_booking_data.csv')

# print(df.isnull().sum())
# pd.set_option('max')
print(df.head())
print(df['country'].value_counts())
df = df.drop('company', axis=1)
#
# print(df.iloc[df['adr'].idxmax()]['name'])
# print(df['adr'].mean().round(2))

print(df.columns)
total_df = len(df)
print(df[df['total_of_special_requests'] == 5][['name', 'email']])
print(round((len(df[df['is_repeated_guest'] > 0])/total_df)*100,2))

print(df['name'].str.split().str[1].value_counts()[:5])

print(df.sort_values(by=['children', 'babies'], ascending=False)['name'])
