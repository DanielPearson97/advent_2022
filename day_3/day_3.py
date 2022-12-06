import pandas as pd
from string import ascii_lowercase, ascii_uppercase
import numpy as np

df_raw = pd.read_csv('data.txt', delimiter=' ', header=None)

letters = ascii_lowercase + ascii_uppercase

letter_mapping = {k:v for (k,v) in zip(letters, range(1,len(letters)+1))}

# Task 1 #
df = df_raw.copy()

df['cont_1'] = df[0].apply(lambda x: x[:int((len(x) / 2))])
df['cont_2'] = df[0].apply(lambda x: x[int((len(x) / 2)):])


def check_containers(container_1, container_2):
    for letter in container_1:
        if letter in container_2:
            return letter


df['wrong_letter'] = df.apply(lambda x: check_containers(x['cont_1'], x['cont_2']), axis=1)

df['values'] = df['wrong_letter'].map(letter_mapping)

print('Total value is of rucksack priorities is: ', df['values'].sum())

# Task 2 #
df = df_raw.copy()

df['group_number'] = np.ceil((df_raw.index + 1) / 3)

df = df.groupby('group_number')[0].apply(' '.join).reset_index()
df[0] = df[0].str.split(' ')


def letter_check(row):
    for letter in row[0]:
        if letter in row[1]:
            if letter in row[2]:
                return letter

df['badge_letter'] = df[0].apply(letter_check)

df['values'] = df['badge_letter'].map(letter_mapping)

print('Total value is of group priorities is: ', df['values'].sum())
