import csv
import time

FILE = "pythonData.csv"

sortTime = 0

array = [0, 2, 5, 3, 4, 1]

data = []

def bubbleSort(array):
    global sortTime
    startTime = time.perf_counter()
    for i in range(len(array)):
            for j in range(0, len(array) - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    sortTime = time.perf_counter() - startTime
                    Time = f"t{sortTime:.10f}"
                    with open(FILE, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(array + [Time])

with open(FILE, mode='w', newline='') as file:
    pass

bubbleSort(array)