import csv
import time

import globalVariables

label = f"a"    # Bubble sort identifier is 'a'

with open(globalVariables.outputFile, mode='w', newline='') as file: # Clear file before sorting
    pass

def bubbleSort(array):
    startTime = time.perf_counter() # Initialize start time
    for i in range(len(array)):
            for j in range(0, len(array) - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    globalVariables.sortTime = time.perf_counter() - startTime          # Update sort time based on current time and start time
                    Time = f"{globalVariables.sortTime:.14f}"                           # Store the sort time as a .14 decimal float
                    with open(globalVariables.outputFile, mode='a', newline='') as file:      # Open file and write to each new line
                        datawriter = csv.writer(file)                   # Initialize the writer for the file
                        datawriter.writerow(array + [Time] + [label])   # Write data to the file

bubbleSort(globalVariables.array)   # Call bubbleSort on the array