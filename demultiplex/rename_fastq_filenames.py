#!/bin/python

import csv
import re
import os
import shutil

dat = "rename_barcode_first_plate.csv"

current_folder = os.getcwd() # get working dir
print os.listdir(current_folder) # list folder contents

# make a dict for match
with open(dat, mode='r') as infile:
    reader = csv.reader(infile)
    match = {rows[0]:rows[1] for rows in reader}

# function to find and replace whole sample names
def replace_all(text, dic):
    for i, j in dic.items():
        text = re.sub(r"\b%s\b"%i, j, text)
        # r"\b%s\b"% enables replacing by whole word matches only
    return text

search_text = r'^foo_([0-9A-Z]+).bam'
ext = (".bam")

# loop through only bam files
for file in os.listdir(current_folder):
    if file.endswith(ext):
        print "orig file = " + file
        old_name = re.sub(search_text, r'\1', file)
        print "old name = " + old_name
        new_name = replace_all(old_name, match)
        print "new name = " + new_name
        old_path = os.path.join(current_folder, file)
        new_path = os.path.join(current_folder, "replace", new_name + ".mmg12.dd.map.bam")
        print old_path
        print new_path
        shutil.move(old_path, new_path)
        print "mooved good yea"
    else:
        continue

print "wow you changed the names of this disaster"
