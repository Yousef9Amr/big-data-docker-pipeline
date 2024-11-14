# -*- coding: utf-8 -*-
"""dpre.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Aa97NUjWIRoAo8O4comDkT21Tctmoe-3
"""

# dpre.py
import pandas as pd

def preprocess_data(input_path, output_path):
    data = pd.read_csv(input_path)

    # Data Cleaning
    data.dropna(inplace=True)
    data.drop_duplicates(inplace=True)

    # Data Transformation
    if 'Name' in data.columns:
        data['Name'] = data['Name'].str.lower()
    if 'Age' in data.columns:
        data['Age'] = data['Age'].fillna(data['Age'].median())

    # Data Reduction
    if 'Ticket' in data.columns:
        data = data.drop(columns=['Ticket'])

    # Data Discretization
    if 'Fare' in data.columns:
        data['Fare_bins'] = pd.cut(data['Fare'], bins=5)

    # Save the processed data
    data.to_csv(output_path, index=False)

if __name__ == "__main__":
    preprocess_data('/home/doc-bd-a1/temp_data.csv', '/home/doc-bd-a1/res_dpre.csv')