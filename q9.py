import pandas as pd
data = pd.read_csv('customerData.csv')
#a
print(data[(data['income']>16000) & (data['state_of_res']=='Washington')]['age'].mean())
#b
print(data['age'].max())
#c
print(data['income'].min())
#d
print(len(data[(data['income']>16000) & (data['state_of_res']=='Washington')]))