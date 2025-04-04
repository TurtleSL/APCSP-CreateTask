import csv
import sys
import pandas

import globalVariables

globalVariables.inputFile = f"../../{sys.argv[1]}"
globalVariables.outputFile = f"../../{sys.argv[2]}"

with open(globalVariables.inputFile, "r") as readfile:      # Open file and write to each new line
    lengthRow = ["Length"]
    datareader = csv.reader(readfile)
    pandas.read_csv(readfile, usecols=lengthRow)