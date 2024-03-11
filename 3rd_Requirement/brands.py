# -*- coding: utf-8 -*-
"""Brands.ipynb

Original file is located at Google Colab

Loading a uncompressed JSON file and normalizing it
"""

import pandas as pd
from pandas import json_normalize
import json

# Replace 'your_file.json' with the actual path to your JSON file
json_file_path = '/content/brands.json'

# Read JSON file line by line into a list
with open(json_file_path, 'r') as file:
    lines = file.readlines()

# Load each line as a separate JSON object
data = [json.loads(line) for line in lines]

# Use json_normalize to flatten the nested structure
brands = json_normalize(data)

# Display the normalized DataFrame
print(brands)

"""Converting JSON file into Excel file for having a structure for the data"""

excel_file_path = 'output_file.xlsx'
brands.to_excel(excel_file_path, index=False)

brands

"""Gaining information about the dataset. Building a brief data dictionary"""

brands.info()

brands["barcode"] = brands["barcode"].astype(str)

"""Quantifying missing data"""

brands.isna().sum()

brands.isna().sum().sum()

percentage_nullvalues = brands.isna().mean()
for key, value in percentage_nullvalues.items():
  if value>0:
    print(key, ":", value * 100)

#More than 50% fraction of the values are missing from topBrand and categoryCode.

"""Checking duplicates"""

duplicates = brands[brands.duplicated()]
print('Duplicat rows except for the first occurences in each column: ')
print(duplicates)

"""Lets make category the target variable."""

#finding unique values inside the category
brands['category'].unique()

brands['category'].nunique()

brands['category'].value_counts()

"""We can conclude from above that majority of the brands belong to Baking category

At last I would like to say that there was one data quality issue in this dataset and that was a large number of missing values in topBrand and categoryCode columns
"""

