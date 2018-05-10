# PDaffy produces a PhenoData file for microarray analysis using the .cel files in the target directory. 
# Default file name input format is "GSM#_GROUP_REP.CEL"

import os
import re

# Get current file directory
cwd = os.getcwd()
os.chdir(cwd)

# Create (empty) celstring list and celext file ext. list
celstring = []
celext = ".CEL",".cel"

# Find files ending in .CEL/.cel and add to celstring list
for f in os.listdir():
    if any(i in f for i in celext):
        celstring.append(f)

# Double-check list is correct
print(celstring)

# Open PhenoData file or create one if does not exist
text_file = open("PhenoData_affy.txt","w+")

# PhenoData Template
text_file.write("Sample ID")
text_file.write("\t")

text_file.write("GroupRep")
text_file.write("\t")

text_file.write("Replicate")
text_file.write("\t")

text_file.write("Group")
text_file.write("\n")

for line in celstring:
    #delimin

    # Sample ID
    text_file.write(line)
    text_file.write("\t")
    
    # GroupRep
    text_file.write(re.split('_|\.', line)[1])
    text_file.write("_")
 
    text_file.write(re.split('_|\.', line)[2])
    text_file.write("\t")

    # Rep

    text_file.write(re.split('_|\.', line)[2])
    text_file.write("\t")

    # Group
    text_file.write(re.split('_|\.', line)[1])
    text_file.write("\n")

# Close the file
text_file.close()

