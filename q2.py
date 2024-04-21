import pandas as pd

#load the data
data = pd.read_csv('customerData.csv')
#describe the data
print(data.describe())
#print the datas dimensions
print("\ndata dimensions:",data.shape,"\n")
#for each colomn print if its numeric or categorical
for col in data.columns:
    if data[col].dtype == 'object':
        print(col, "is categorical")
    else:
        print(col, "is numeric")
        
#why customerID is not relevant to the analysis
#CustomerID is not relevant to the analysis because it is a unique identifier for each customer and does not provide any useful information for analysis



