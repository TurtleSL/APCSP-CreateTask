import csv
import time

import globalVariables

label = f"bubble"    # Bubble sort identifier is 'a'

outputData = []

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

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
                    globalVariables.addDataToOutput(array, outputData, Time, label)

globalVariables.createHeaders(array, outputData)
print(outputData)
bubbleSort(globalVariables.array)   # Call bubbleSort on the arraya