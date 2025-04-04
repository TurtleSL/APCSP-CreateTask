import csv
import sys

import globalVariables

globalVariables.inputFile = f"../../{sys.argv[1]}"
globalVariables.outputFile = f"../../{sys.argv[2]}"

print(globalVariables.outputFile)

with open(globalVariables.outputFile, "r") as readfile:      # Open file and write to each new line
    datareader = csv.reader(readfile)
    for row in datareader:
        print(row)