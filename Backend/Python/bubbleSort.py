import csv
import time

import globalVariables

label = f"bubble"

output = []

with open(globalVariables.outputFile, mode='w', newline='') as file: # Clear file before sorting
    pass

def bubbleSort(array, length):
    startTime = time.perf_counter()
    globalVariables.createHeaders(array, output)
    for i in range(length):
        for j in range(0, length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                globalVariables.sortTime = time.perf_counter() - startTime
                Time = f"{globalVariables.sortTime:.14f}"
                globalVariables.addDataToOutput(array, Time, label, output)

    with open(globalVariables.outputFile, "w", newline='') as file:
        datawriter = csv.writer(file)
        datawriter.writerows(output)        # Write rows to ouput file