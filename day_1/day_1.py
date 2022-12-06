import pandas as pd

# PART 1
with open('data.txt') as f:
    lines = f.readlines()
lines=[x.replace('\n','') for x in lines]
df = pd.DataFrame(lines).rename(columns={0:'calorie_amount'})
count=0
calories=[]
for index, key in df.iterrows():
    if key['calorie_amount']!='':
        count = count+int(key['calorie_amount'])
    else:
        calories.append(count)
        count=0
print('The max calories are: ', max(calories))
# PART 2
count = 0
for i in range(3):
    count = count+max(calories)
    calories.remove(max(calories))
print('The calories of the max three are: ', count)