import numpy as np
import pandas as pd


demand_sheet = pd.read_excel('/Users/vishnu.tiwari/Desktop/Python/'
                             'Machine Learning and Data Science/Pandas/'
                             'demandsheet_operations/'
                             'dem_sheet.xlsx')
# print(demand_sheet)
columns = list(demand_sheet.columns)
# print(columns)
input_primary_skill = str(input('Enter the primary key to search \n'))
input_primary_skill= input_primary_skill.split(', ')
prim_skills = ((demand_sheet['Primary Skills'].isin(input_primary_skill)) | (demand_sheet['Secondary Skills'].isin(input_primary_skill))) & (demand_sheet['Experience'].isin(['0-2.5 Years','2.5-5 Years']))


resultant_index = list(demand_sheet[prim_skills].index)

for index, value in enumerate(resultant_index):
    print(f'{index}. Primary Skill = {demand_sheet.iloc[value]["Primary Skills"]}')
    print(f'   Secondary Skill = {demand_sheet.iloc[value]["Secondary Skills"]}')
    print(f'   Band {demand_sheet.iloc[value]["Band"]}')
    print(f'   Designation = {demand_sheet.iloc[value]["Designation"]}')
    print(f'   Experience Required: {demand_sheet.iloc[value]["Experience"]}')
    print(f'   Sub Band: {demand_sheet.iloc[value]["Sub band"]}')
    print(f'   Project Name: {demand_sheet.iloc[value]["Project"]} ')
    print(f'   Country: {demand_sheet.iloc[value]["country"]}')
    print(f'   Job : {demand_sheet.iloc[value]["Job"]}')
    print(f'   State : {demand_sheet.iloc[value]["Personal SubArea"]}')
    print(f'   Initiator = {demand_sheet.iloc[value]["Initiator"]}')
    print(f'   Row Details = {value-2}')
    print(f'   Job Description = {demand_sheet.iloc[value]["Job Description"]}')
    print(f'********************************************')
    print(f'********************************************')


print(input_primary_skill)



print(demand_sheet.iloc[resultant_index[5]]['Initiator'])

# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_colwidth', None)
# pd.set_option('display.width', 1000)