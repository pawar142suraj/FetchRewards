# -*- coding: utf-8 -*-
"""Receipts.ipynb

Original file is located at Google Colab

Loading a uncompressed JSON file and normalizing it
"""

import pandas as pd
from pandas import json_normalize
import json

# Replace 'your_file.json' with the actual path to your JSON file
json_file_path = '/content/receipts.json'

# Read JSON file line by line into a list
with open(json_file_path, 'r') as file:
    lines = file.readlines()

# Load each line as a separate JSON object
data = [json.loads(line) for line in lines]

# Use json_normalize to flatten the nested structure
receipts = json_normalize(data)

# Display the normalized DataFrame
print(receipts)

excel_file_path = 'output_file.xlsx'
receipts.to_excel(excel_file_path, index=False)

receipts.info()

receipts.isna().sum()

receipts.isna().sum().sum()

percentage_null_values= receipts.isnull().mean()
for key,value in percentage_null_values.items():
  if value >0:
    print(key,":",value*100)

"""A considerate fraction of values are missing from the above mentioned variables. Missing values for certain
variables are a major concern:
finishedDate- for 49%(almost half) of the receipts we don't know when do they become invalid(assuming that the
date on which a receipt finishes processing is the date on which it becomes invalid)

"""

receipts["pointsEarned"].unique()

receipts["pointsEarned"].nunique()

"""pointsEarned- 45% of the values for the 'pointsEarned' field are missing. If we look at the unique values for
'pointsEarned', we do not have a zero value. This means that points were earned for certain receipts but the data
was not captured and that's why the large number of missing values.
purchasedItemCount- large number of missing values will pose problems for deciding if users who bought more
than one unit of a product qualify for special offers/bonus points that require them to purchase certain amount of
particular products/brands.
totalSpent, rewardsReceiptItemList- Since data for these two fields is missing, it is natural that we don't have
information about points earned(pointsEarned field) for those transactions.

Checking the correlation
"""

receipts.corr()

#there is no significant correlations found

