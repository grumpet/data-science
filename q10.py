import pandas as pd
#load the data
data = pd.read_csv('customerData.csv')
df = data[['housing_type', 'gender']]
df_females = df[df['gender'] == 'F']
df_females = df['housing_type'].value_counts()
print('most popular female housing type',df_females.max())
df_male = df[df['gender'] == 'M']
df_male = df['housing_type'].value_counts()
print('most popular male housing type',df_male.max())   
