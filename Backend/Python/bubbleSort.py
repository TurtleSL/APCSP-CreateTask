import csv
import time

import globalVariables

label = f"bubble"    # Bubble sort identifier is 'a'

array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

output = []

with open(globalVariables.outputFile, mode='w', newline='') as file: # Clear file before sorting
    pass

def bubbleSort(array):
    startTime = time.perf_counter()
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                globalVariables.sortTime = time.perf_counter() - startTime
                Time = f"{globalVariables.sortTime:.14f}"
                globalVariables.addDataToOutput(array, Time, label, output)

    with open(globalVariables.outputFile, "w", newline='') as file:
        datawriter = csv.writer(file)
        datawriter.writerows(output)

globalVariables.createHeaders(array, output)
bubbleSort(array)   # Call bubbleSort on the array