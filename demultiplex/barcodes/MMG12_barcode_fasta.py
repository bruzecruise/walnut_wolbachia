#!/bin/python
import sys
import csv
import re
import pandas as pd

# import csv
# select plates (filter out other plates)
# create fasta file for ecoR1 - read1 barcode
# create fata file for MSEI  - read2 barcode

# enter params
# 1 = csv file with old barcode name in col 1 and new name in col2
# 2 tab delimited barcode file with ID and barcode columns. ID must match that of above csv
# data = sys.argv[1]
data = "rename_files_firstRun.csv"

# barcode_txt = sys.argv[2]
barcode_txt = pd.read_csv("barcodes.MMG.1.2.fixed.txt", sep='\t')
# barcode_txt = barcode_txt.reset_index()

# open out files
fasta_barcode = open("barcode1_R1.fasta", "w")


with open(data, mode='r') as infile:
    reader = csv.reader(infile)
    match = {rows[0]:rows[1] for rows in reader}


# function to find and replace whole sample names
def replace_all(text, dic):
    for i, j in dic.items():
        text = re.sub(r"\b%s\b"%i, j, text)
        # r"\b%s\b"% enables replacing by whole word matches only
    return text


for index, row in barcode_txt.iterrows():
    rep = replace_all(row['ID'], match)
    barcode_txt.at[index, 'New_ID'] = rep
print "loop over"
print barcode_txt

for index, row in barcode_txt.iterrows():
    fasta_barcode.write(">" + row['New_ID'] + "\n" + row['barcode'] + "\n")

fasta_barcode.close()