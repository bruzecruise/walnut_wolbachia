#!/bin/python

import sys
import re

fastq_file = sys.argv[1]
fastq_RegEx = re.compile("fq")
fastq_file_fix = re.sub(fastq_RegEx, "fixed.fq", fastq_file)

fastq = open(fastq_file, "r")
outfile = open(fastq_file_fix, "w")

search_text = r'(^@[0-9]+_)'

for line in fastq:
    line = line.strip()
    if "@" in line:
        line = re.sub(search_text, "@", line)
        line = re.sub(r'(mmg.)', "", line)
        line = re.sub(r'(HS[.]*)', "HS", line)
        line = re.sub(r'(HS[0-9]+)([.]*)', r'\1', line)
        line = re.sub(r'(SPE[.]+)', "SPE", line)
        outfile.write(line + "\n")
    else:
        outfile.write(line + "\n")

outfile.close()
fastq.close()

print ("finished fixing read names!")

# need to pfix match groups
