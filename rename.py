import sys
import re
import pandas as pd


# Read in the file to have its strings replaced
with open('ComboL.txt', 'r') as file :
  filedata = file.read()

# read in dataframe with original and replacement columns
names = pd.read_csv("rename.csv")

# loop through replacement dataframe and replace strings in file
for index, row in names.iterrows():
    old = row['name']
    new = row['new_name']
    filedata = filedata.replace(old, new)

# Write the file out
with open('test.txt', 'w') as file:
  file.write(filedata)