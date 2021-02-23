import pandas as pd
import numpy as np
import os

# Read from trajectory raw data from PHR
df = pd.read_csv(r'D:\thomas\project\WELL_TRAJECTORY_DURI.csv')

# Read well header from PHR
well_info =  pd.read_excel(r'D:\#DURI-\1. Data\Well Header info.xlsx', sheet_name=1, skiprows=1)

# Make a list of Survey Source
survey_sources = list(set(df['SURVEY_SOURCE']))

# Make a function to check type of well based on source and prints number of wells
def well_source(df=df, identifier='UWI',survey_sources=survey_sources):
    '''Create a report of wells based on survey sources and 
    prints the number of wells associated with it.

    df
    identifier
    survey_sources
    '''
    for source in survey_sources:
        survey = df[df.SURVEY_SOURCE == source]
        num_of_wells = len(list(set(survey[identifier])))
        print('Number of wells from {}: {}'.format(source, num_of_wells))

# Make a function to count wells based on name/UWI to define horizontal/deviated wells
def well_dev(df=df, identifier='UWI', strings=['D1', 'H1']):
    well_uwi = []
    for string in strings:
        df_dev = df.loc[df[identifier].str.contains('H1', na=False)]
        num_of_wells = len(list(set(df_dev[idetifier])))
        print('{} wells: {}'.format(string, num_of_wells))

