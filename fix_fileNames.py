import sys
import re

sam_file = sys.argv[1]
samRegEx = re.compile("sam")
sam_file_fix = re.sub(samRegEx, "fixed.sam", sam_file)


sam = open(sam_file, "r")
outfile = open(sam_file_fix, "w")

search_text = r'(^[0-9]+_)'

for line in sam:
    line = line.strip()
    if "@" in line:
        outfile.write(line + "\n")
    else:
        line = re.sub(search_text, "", line)
        line = re.sub(r'(^mmg.)', "", line) 
        line = re.sub(r'(^HS.)', "HS", line)
        line = re.sub(r'(^SPE[.]+)', "SPE", line)
        outfile.write(line + "\n")
outfile.close()
sam.close()

print ("finished fixing read names!")

