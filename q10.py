import pandas as pd
#load the data
df = pd.read_csv('customerData.csv')

group10 = df[['gender','housing_type']]
#Q10a
group10_female = group10[group10['gender']=='F']
group10_female = group10_female.groupby('housing_type').size()
most_popular_housing_type = group10_female.idxmax()
print(most_popular_housing_type)
#Q10b
man_group = df[df["gender"] == "M"]
group = man_group.groupby("housing_type").size()
most_popular_housing_type_male = group.idxmax()
print(most_popular_housing_type_male)