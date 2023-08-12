import pandas as pd 
dataset=pd.read_csv(r'country_vaccinations.csv')
print("shape of given data set:",dataset.shape)
print("count of column:",len(dataset.column))
print("name of parameter used:",dataset.column)
print("display empty row data:",dataset.loc[:,dataset.isna().any()])