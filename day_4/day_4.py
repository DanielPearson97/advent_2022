import pandas as pd
import numpy as np

df = pd.read_csv('data.txt', header=None).rename(columns={0: 'as_1', 1: 'as_2'})

df['as_1_l'] = df['as_1'].str.split('-').str[0].astype(int)
df['as_1_h'] = df['as_1'].str.split('-').str[1].astype(int)

df['as_2_l'] = df['as_2'].str.split('-').str[0].astype(int)
df['as_2_h'] = df['as_2'].str.split('-').str[1].astype(int)

# Task 1 #

condition_1 = (
        ((df['as_1_l'] >= df['as_2_l']) & (df['as_1_h'] <= df['as_2_h']))
        |
        ((df['as_2_l'] >= df['as_1_l']) & (df['as_2_h'] <= df['as_1_h']))
)

df['first_check'] = np.where(condition_1, 1, 0)

print('The number of fully overlapping pairs is: ', df['first_check'].sum())

# Task 2 #

condition_2 = (
    ~((df['as_2_h'] < df['as_1_l']) | (df['as_1_h'] < df['as_2_l']))
)

df['second_check'] = np.where(condition_2, 1, 0)

print('The number of fully partially pairs is: ', df['second_check'].sum())