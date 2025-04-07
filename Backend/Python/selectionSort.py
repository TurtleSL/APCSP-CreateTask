import csv
import time

import globalVariables

label = f"selection"

output = []

with open(globalVariables.outputFile, mode='w', newline='') as file: # Clear file before sorting
    pass

def selectionSort(array, length):
    for i in range(length - 1):
        min = i
        for j in range(i + 1, length):
            if array[j]