import csv
import sys

import globalVariables
import bubbleSort

globalVariables.inputFile = f"../../{sys.argv[1]}"
globalVariables.outputFile = f"../../{sys.argv[2]}"

tempArray = []

with open(globalVariables.inputFile, "r") as readfile:      # Open file and write to each new line
    datareader = csv.DictReader(readfile)
    for row in datareader:
        length = int(row["Length"])
        for i in range(length):
            temp = int(row[f"A{i}"])
            tempArray.append(temp)
    
        if row["Type"] == "bubble":
            bubbleSort.bubbleSort(tempArray)
            print(tempArray)
        else:
            print("Sort not available")