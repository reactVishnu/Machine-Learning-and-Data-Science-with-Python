import importlib

# Check if pandas is installed
try:
    importlib.import_module('pandas')
    pandas_installed = True
except ImportError:
    pandas_installed = False

if not pandas_installed:
    print("Pandas is not installed. Installing...")

    try:
        # Install pandas using pip
        import subprocess

        subprocess.check_call(['pip', 'install', 'pandas'])
        print("Pandas has been successfully installed.")
    except Exception as e:
        print("An error occurred while installing Pandas:", str(e))
        exit(1)

import pandas as pd

# Opening the Demand Sheet
demand_sheet = pd.read_excel('dem_sheet.xlsx')
columns = list(demand_sheet.columns)

input_primary_skill = str(input('Enter the primary skill to search \n'))
input_primary_skill = input_primary_skill.split(',')
input_experience = float(input('Enter the year of experience \n'))
input_location = str(
    input('Enter your location (eg: Noida, Pune, Chennai - type "any" if you good for any location) \n'))
input_location = input_location.split(',')

p_skill = []
for i in input_primary_skill:
    p_skill.append(i.strip())
input_primary_skill = p_skill


def find_experience_ranges(experience):
    ranges = []
    if 11 <= experience <= 15:
        ranges.append("11-15 Years")
    if 7.5 <= experience <= 12:
        ranges.append("7.5-12 Years")
    if 7 <= experience <= 12:
        ranges.append("7-12 Years")
    if 5 <= experience <= 9:
        ranges.append("5-9 Years")
    if 4.5 <= experience <= 8:
        ranges.append("4.5-8 Years")
    if 2.5 <= experience <= 5:
        ranges.append("2.5-5 Years")
    if 0 <= experience <= 2.5:
        ranges.append("0-2.5 Years")
    if not ranges:
        return "Experience out of range"
    return ranges


input_experience = find_experience_ranges(input_experience)

stripped_skill = []


def secondary_skill_checker(secondary_skill):
    # print(secondary_skill)
    for skill in input_primary_skill:
        if skill in str(secondary_skill):
            # stripped_skill.append(skill.strip())
            return True
    return False




def location_checker(location):
    if input_location[0] == 'any' or input_location[0] == 'Any' or input_location[0] == 'ANY':
        return True
    for loc in input_location:
        if loc in str(location):
            return True
    return False


demand_sheet['location_found'] = demand_sheet['Personal SubArea'].apply(location_checker)
demand_sheet['secondary_skill_found'] = demand_sheet['Secondary Skills'].apply(secondary_skill_checker)
demand_sheet['primary_skill_found'] = demand_sheet['Primary Skills'].apply(secondary_skill_checker)
prim_skills_first = (demand_sheet['primary_skill_found']) | (demand_sheet['secondary_skill_found'])
location_plus_skill = prim_skills_first & (demand_sheet['location_found'])
prim_skills = location_plus_skill & (demand_sheet['Experience'].isin(input_experience))

resultant_index = list(demand_sheet[prim_skills].index)

for index, value in enumerate(resultant_index):
    print(f'{index}. Req No. = {demand_sheet.iloc[value]["ReqNo"]}')
    print(f'   Primary Skill = {demand_sheet.iloc[value]["Primary Skills"]}')
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
    print(f'   Row Details = {value - 2}')
    print(f'   Job Description = \n'
          f'   {demand_sheet.iloc[value]["Job Description"]}')
    print(f'********************************************')
    print(f'********************************************')

print(input_primary_skill, input_experience, input_location)








