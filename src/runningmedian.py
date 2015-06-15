#uses Python v3.4 for the statistics package
#Author: Beno Varghese

import glob, os, re
from collections import Counter, defaultdict
from sys import argv
from statistics import median

#Get input path from command line and search for text files within the file path.
inputFiles =   glob.glob(os.path.join(argv[1], "*.txt"))
outputFile =   ".\wc_output\med_result.txt"  #write output to the directory and file specified here.
arrayMedian = [] #array to hold median values

#for each file  in the input directory, open and read it. Then open the output file for append.
for file in inputFiles:
    openReadFile = open(file,"r")
    openWriteFile = open(outputFile, "a")

    # for each line in the input file, cleanup the line, split it and count the number of words in each line.
    # Append the count to an array and take the median of the values in the array and then output to a file.
    for line in openReadFile:
         processLine = len(re.sub('[^a-z\ \']+', "\t", line).split())
         arrayMedian.append(processLine)
         runningMedian = median(arrayMedian)
         openWriteFile.write('{:.1f}\n'.format(runningMedian))
    
    #cleanup - close all open files.
    openReadFile.close()
    openWriteFile.close()