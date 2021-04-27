#!/bin/python

import re
import sys
import pandas as pd

sam_file = sys.argv[1]

samRegEx = re.compile("sam")
csv_file = re.sub(samRegEx, "count_metadata.csv", sam_file)


# loop through and create a set with all the regex hits.
# use a set to only get unique regex hits
addresses = set()
pattern = re.compile(r'^[0-9A-Za-z.]+_')

with open(sam_file, 'r') as f:
    for line in f:
        match = pattern.match(line)
        if match is not None:
            addresses.add(match.group())

for address in sorted(addresses):
    print(address)

# this is the monies loop
# # loop through set from above and count number of occurrences in file
samples = {}
count = 0
for n in addresses:
    # print (n)
    with open(sam_file, 'r') as f:
        count = 0
        for line in f:
            if n in line:
                count += 1
        samples[n] = count
        # print(count)

# print(samples)

# make csv file for the count data
df = pd.DataFrame.from_dict(samples, orient='index').reset_index()
df.columns = ['name','count']
sorted_df = df.sort_values(by=['count'], ascending=False)


sel_dat = sorted_df[['name', 'count']]
sel_dat['name'] = sel_dat['name'].str.replace(r'_', "")
metadata = pd.read_csv("barcode_1_metadata.csv")

merged_dat = pd.merge(sel_dat, metadata, on='name')
merged_dat.to_csv(csv_file)

print(merged_dat)

print("finished counting reads!")
