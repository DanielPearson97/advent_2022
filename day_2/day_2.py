import pandas as pd

df_raw = pd.read_csv('data.txt', delimiter=' ', header=None).rename(columns={0: 'opp', 1: 'self'})

# TASK 1 #

df = df_raw.copy()

self_use_map = {'X': 1, 'Y': 2, 'Z': 3}

df['self_score'] = df['self'].map(self_use_map)


def get_winner(opp, self):
    win_condition = (opp == 'A' and self == 'Y') | (opp == 'B' and self == 'Z') | (opp == 'C' and self == 'X')
    draw_condition = (opp == 'A' and self == 'X') | (opp == 'B' and self == 'Y') | (opp == 'C' and self == 'Z')
    loss_condition = (opp == 'A' and self == 'Z') | (opp == 'B' and self == 'X') | (opp == 'C' and self == 'Y')

    if win_condition:
        return 6
    elif draw_condition:
        return 3
    elif loss_condition:
        return 0


df['game_score'] = df.apply(lambda x: get_winner(x['opp'], x['self']), axis=1)

df['total_score'] = df['self_score'] + df['game_score']

print('The total score for this strategy is ', df['total_score'].sum())

# TASK 2 #

df = df_raw.copy()

df = df.rename(columns={'self': 'result'})

self_use_map = {'X': 0, 'Y': 3, 'Z': 6}

df['game_score'] = df['result'].map(self_use_map)


def get_response(opp, result):
    rock_condition = (result == 'Z' and opp == 'C') | (result == 'Y' and opp == 'A') | (result == 'X' and opp == 'B')
    paper_condition = (result == 'Z' and opp == 'A') | (result == 'Y' and opp == 'B') | (result == 'X' and opp == 'C')
    scissor_condition = (result == 'Z' and opp == 'B') | (result == 'Y' and opp == 'C') | (result == 'X' and opp == 'A')

    if rock_condition:
        return 1
    elif paper_condition:
        return 2
    elif scissor_condition:
        return 3


df['self_score'] = df.apply(lambda x: get_response(x['opp'], x['result']), axis=1)

df['total_score'] = df['self_score'] + df['game_score']

print('The total score for this strategy is ', df['total_score'].sum())
