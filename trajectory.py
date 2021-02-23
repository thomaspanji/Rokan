import pandas as pd
import numpy as np
import os

# Read from raw data from PHR
df = pd.read_csv(r'D:\thomas\project\WELL_TRAJECTORY_DURI.csv')

# Make a list of unique wellname
wellname = list(set(df['UWI']))

for well in wellname:
    per_well = df[['UWI', 'MD', 'AZIMUTH', 'INCLINATION']].loc[df['UWI'] == well]
    per_well.to_csv(r'D:\thomas\project\duri\{}.csv'.format(well), index=False)