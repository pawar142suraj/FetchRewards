# -*- coding: utf-8 -*-
"""Users.ipynb

Original file is located at Google Colab

Loading a uncompressed JSON file and normalizing it
"""

import pandas as pd
from pandas import json_normalize
import json

# Replace 'your_file.json' with the actual path to your JSON file
json_file_path = '/content/users.json'

# Read JSON file line by line into a list
with open(json_file_path, 'r') as file:
    lines = file.readlines()

# Load each line as a separate JSON object
data = [json.loads(line) for line in lines]

# Use json_normalize to flatten the nested structure
users = json_normalize(data)

# Display the normalized DataFrame
print(users)

excel_file_path = 'output_file.xlsx'
users.to_excel(excel_file_path, index=False)

users

users.info()

users["lastLogin.$date"] = users["lastLogin.$date"].astype(str)

users.isna().sum()

users.isna().sum().sum()

percentage_null_values= users.isnull().mean()
for key,value in percentage_null_values.items():
  if value >0:
    print(key,":",value*100)

duplicateRowsDF = users[users.duplicated()]
print("Duplicate Rows except first occurrence based on all columns are :")
print(duplicateRowsDF)

#there is are a large number of duplicate values in this dataset

users["role"].unique()

users["signUpSource"].unique()

users["state"].unique()

users['signUpSource'].value_counts()

users['state'].value_counts()

"""As per this data, majority of the users that have signed up reside in Wisconsin.
Data quality issues found:
1. More than half of the user records(out of the total 495) are redundant.
Another, less pressing issue:
1. small percentage of missing values in signUpSource and state columns
"""

