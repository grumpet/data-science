#q5
import pandas as pd

#load the data
data = pd.read_csv('customerData.csv')
#create a new dataframe with only people who are older than 38 and younger then 50
data2 = data[(data['age'] > 38) & (data['age'] < 50)]
#q6 
# a
# data3 should have all the people who are older than 50 and only numeric columns
data3 = data[(data['age'] > 50)]
data3 = data3.select_dtypes(include='number')
print(data3)
# b
data4 = data[(data['age'] > 50)]
data4 = data4.select_dtypes(include='number')
data4.columns = range(data4.shape[1])
print(data4)
#q7
data5 = pd.DataFrame(data4[3]).head(100)
print(data5)


