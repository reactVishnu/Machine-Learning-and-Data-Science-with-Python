# import numpy as np
import pandas as pd

my_list = [1947, 1988, 1999, 2002]
my_index = ['India', '', 'Reservation', 'Vishnu']

my_first_panda_series = pd.Series(my_list, my_index)
print(my_first_panda_series)
print(my_first_panda_series['Vishnu'])

age = {
    'Vishnu': 20,
    'Simi': 23,
    'Deepak': 28,
}
age_series = pd.Series(age)
print(age_series['Deepak'])
# print(age[0])


q1_sales = {'India': 200, 'Pakistan':  123, 'China': 300, 'Bangladesh': 100}
q2_sales = {'India': 250, 'Pakistan': 134, 'China': 400, 'Srilanka': 75}

q1_sales = pd.Series(q1_sales)
q2_sales = pd.Series(q2_sales)

first_half = q1_sales + q2_sales

print(first_half)
print(q1_sales.keys())

print(q1_sales.add(q2_sales, fill_value=0))

first_half = pd.Series(first_half, dtype='int64')
print(first_half)