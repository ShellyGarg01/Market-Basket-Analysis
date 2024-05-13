import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('D:\TRU\sem last\Power-Bi-Exercise\project\Market Basket Analysis_Data.csv\MSB_Data.csv', sep=';',parse_dates=['Date'])
# print(data.head())

#Data pre processing:

#changing the data type of price column from object to float64
data['Price'] = data['Price'].str.replace(',','.').astype('float64')
# print(data.info())

#calculating the number of missing values
# print(data.isna().sum().sort_values(ascending=False))

data['Total_Price'] = data.Quantity * data.Price

# print(data.describe(include= 'all'))

# print("Number of unique countries : ", data['Country'].nunique())
# print(data['Country'].value_counts(normalize=True)[:5])

data.drop('Country', axis=1, inplace=True)

# print(data[data['BillNo'].str.isdigit() == False])

data = data[data['Itemname'] != "Adjust bad debt"]

# print(data['BillNo'].astype("int64"))

# print(data[data['Itemname'].isna()])

#the above print statement showed that we have 1455 rows where item name is missing so we will drop these rows
data = data[data['Itemname'].notna()]

#printing the number of unique items in the itemname column
# print("Number of unique items: ", data['Itemname'].nunique())
# print(data['Itemname'].value_counts(normalize=True)[:5])

# print(data[data['Quantity']< 1])
#removing rows with quantity less than 1
data = data[data['Quantity'] >=1]

# print(data[data['CustomerID'].isna()].sample(30))

#counting the number of rows where price is 0 or negaive

# zero_price_count = len(data[data['Price'] == 0 ])
# print("Number of rows where price is zero: ", zero_price_count)
# negative_price_count = len(data[data['Price'] < 0])
# print("Number of rows where price count is negative: ", negative_price_count)

#removing rows where price is 0
data = data[data['Price'] != 0]

# data.to_csv('preprocessed_data.csv', index=False)

#Now creating association rules

data_2 = data

#filtring rows based on the occurences of item (item apprearring more than once)
item_counts = data_2['Itemname'].value_counts(ascending=False)
filtered_items = item_counts.loc[item_counts > 1].reset_index()['index']
data_2 = data_2[data_2['Itemname'].isin(filtered_items)]

#filtering for bill number occurences
bill_count = data_2['BillNo'].value_counts(ascending=False)
filtered_bills = bill_count.loc[bill_count > 1].reset_index()['index']
data_2 = data_2[data_2['BillNo'].isin(filtered_bills)]

#now creating a pivot table  to generate the rules
pivot_table = pd.pivot_table(data_2[['BillNo', 'Itemname']], index='BillNo', columns = 'Itemname', aggfunc=lambda x: True, fill_value=False)

# importing apriori

from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

frequent_itemsets = apriori(pivot_table, min_support=0.02, use_colnames=True)

rules = association_rules(frequent_itemsets, "confidence", min_threshold= 0.5)

print("Frequent Itemsets:")
print(frequent_itemsets)

print("\nAssociation rules: ")
# print(rules)

rules = rules.sort_values(['confidence', 'lift'], ascending=False)
rules = rules.sort_values(by='support', ascending=False)

print(rules)

#exporting these assocaition rules to a csv file
# rules.to_csv('association_rules.csv', index=False)

rules['antecedents'] = rules['antecedents'].apply(lambda x: ', '.join(list(x)))
rules['consequents'] = rules['consequents'].apply(lambda x: ', '.join(list(x)))

# Save the DataFrame to CSV without index
# rules.to_csv('association_rules.csv', index=False)
