import csv
import sys

import globalVariables
import bubbleSort
import mergeSort

globalVariables.inputFile = f"../../{sys.argv[1]}"
globalVariables.outputFile = f"../../{sys.argv[2]}"

tempArray = []

with open(globalVariables.inputFile, "r") as readfile:      # Open file and write to each new line
    datareader = csv.DictReader(readfile)
    for row in datareader:
        length = int(row["Length"])                     # Check for row with "Length" tag
        for i in range(length):
            temp = int(row[f"A{i}"])                    # Check for row with "A#" tag
            tempArray.append(temp)
    
        if row["Type"] == "bubble":                     # Check for sort type
            bubbleSort.bubbleSort(tempArray)
        elif row["Type"] == "merge":
            mergeSort.mergeSort(tempArray, 0, length - 1)
            print(tempArray)
        else:
            print("Sort not available")