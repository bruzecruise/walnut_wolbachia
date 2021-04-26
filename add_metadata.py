import re
import sys
import pandas as pd

df = pd.read_csv("single_end.test.fixed.count.csv")

sel_dat = df[['name', 'count']]

sel_dat['name'] = sel_dat['name'].str.replace(r'_', "")

metadata = pd.read_csv("barcode_1_metadata.csv")

merged_dat = pd.merge(sel_dat, metadata, on='name')
print(merged_dat)


merged_dat.to_csv("test.csv")
