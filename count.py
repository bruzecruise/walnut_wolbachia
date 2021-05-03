#!/bin/python

# this counts the number of reads for each individual
# inputs are 1 = fixed samfile and 2 = metadata csv
import re
import sys
import pandas as pd

# load in files. Need input same file that has had its file names fixed.
# and csv file with metadata for the barcodes
sam_file = sys.argv[1]
input_csv = sys.argv[2]

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
df.columns = ['name', 'count']
sorted_df = df.sort_values(by=['count'], ascending=False)

# fix headers and sort data frame
sel_dat = sorted_df[['name', 'count']]
sel_dat['name'] = sel_dat['name'].str.replace(r'_', "")
sel_dat['name'] = sel_dat['name'].astype(int)

# import metadata csv
metadata = pd.read_csv(input_csv)
metadata['name'] = metadata['name'].astype(int)

# merge dataframes with inner join
merged_dat = pd.merge(sel_dat, metadata, how='inner', on='name')
merged_dat.to_csv(csv_file)

print(merged_dat)
print("finished counting reads!")