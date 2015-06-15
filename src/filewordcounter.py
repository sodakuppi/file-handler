#Author: Beno Varghese

import glob, os, re
from collections import Counter
from sys import argv


#Get input file path from command line and search for text files within the folder specified.
inputFiles =   glob.glob(os.path.join(argv[1], "*.txt"))
outputFile =   argv[2]  #get output file path and name from command line

#for each file in the folder specified, open and read it. Then, convert the words to lower case, clean up the line
# and split up the words. Now, count the number of times each word appears in the file.
for file in inputFiles:
    openReadFile = open(file,"r") 
    processFile = Counter((re.sub('[^a-z\ \']+', "\t", openReadFile.read().lower()).split()))
    openReadFile.close() #cleanup - close input file

    #open output file for writing. For each item, sort it and write to the output file
    openWriteFile = open(outputFile, "w")
    for item in sorted(processFile.items()): 
        openWriteFile.write("{}\t\t{}\n".format(*item))
    openWriteFile.close() #cleanup - close output file

