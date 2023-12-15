import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

unique_values = data['whoAmI'].unique()

one_hot_encoded = {}

for value in unique_values:
    one_hot_encoded[value] = [1 if x == value else 0 for x in data['whoAmI']]

for key, value in one_hot_encoded.items():
    data[key] = value

data.drop('whoAmI', axis=1, inplace=True)

print(data.head())
