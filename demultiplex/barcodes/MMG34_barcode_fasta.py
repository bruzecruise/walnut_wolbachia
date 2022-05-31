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
## barcode_txt = pd.read_csv("barcodes.fixed.txt", sep='\t')
# barcode_txt = barcode_txt.reset_index()

# open out files
fasta_barcode = open("barcode1_R1.fasta", "w")

########### fix barcode file ugh
oldbarcode = open("barcodes.MMG.3.4.txt", "r")
outfile = open("fixed_barcode_MMG34.txt", "w")

search_text = r'(^@[0-9]+_)'

outfile.write("barcode" + "\t" +"ID" + "\n")

for line in oldbarcode:
    line = line.strip()
    line = re.sub(search_text, "@", line)
    line = re.sub(r'(mmg.)', "", line)
    line = re.sub(r'(HS[.]*)', "HS", line)
    line = re.sub(r'(HS[0-9]+)([.]*)', r'\1', line)
    line = re.sub(r'(SPE[.]+)', "SPE", line)
    outfile.write(line + "\n")

outfile.close()
oldbarcode.close()
print ("finished fixing barcode names!")

barcode_txt = pd.read_csv("fixed_barcode_MMG34.txt", sep='\t')
print barcode_txt

# open out fasta file
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


