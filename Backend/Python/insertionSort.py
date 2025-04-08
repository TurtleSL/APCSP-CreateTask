import csv
import time

import globalVariables

label = f"insertion"

output = []

with open(globalVariables.outputFile, mode='w', newline='') as file: # Clear file before sorting
    pass

def insertionSort(array, length):
    for i in range(1, length - 1):
        key = array[i]
