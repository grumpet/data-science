import pandas as pd
#load the data
data = pd.read_csv('customerData.csv')
# print the customerid of the people who are under 18 and their marital_stat is Married or Divorced/Separated
print(data[(data['age']<18) & ((data['marital_stat'] == 'Married') | (data['marital_stat'] == 'Divorced/Separated'))]['custid'])