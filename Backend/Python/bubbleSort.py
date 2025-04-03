import csv
import time

FILE = "pythonData.csv" # FIXME!!! Use a global file to store this

sortTime = 0    # Initialize sort time 

array = [0, 2, 5, 3, 4, 1]  # Example array give, may need to be parsed from front end at some point

label = f"a"    # Bubble sort identifier is "a"

def bubbleSort(array):
    global sortTime # FIXME!!! Use a global file to store this
    startTime = time.perf_counter() # Initialize start time
    for i in range(len(array)):
            for j in range(0, len(array) - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    sortTime = time.perf_counter() - startTime      # Update sort time based on current time and start time
                    Time = f"t{sortTime:.14f}"                      # Store the sort time as a .14 decimal float
                    with open(FILE, mode='a', newline='') as file:  # Open file and write to each new line
                        writer = csv.writer(file)                   # Initialize the writer for the file
                        writer.writerow(array + [Time] + [label])   # Write data to the file

with open(FILE, mode='w', newline='') as file: # Clear file before sorting
    pass

bubbleSort(array)   # Call bubbleSort on the array