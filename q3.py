import pandas as pd

#load the data
data = pd.read_csv('customerData.csv')
#create a new dataframe with only even columns and rows that are divisible by 10
data2 = data.iloc[::10,::2]
#q4
print(data2.shape)
print(data2.size)
# the shape describes the dimensions of the data, the size describes the number of elements in the data
# the shape of data2 is (100,6) and the size is 600
# the size is equal to the product of the dimensions of the data