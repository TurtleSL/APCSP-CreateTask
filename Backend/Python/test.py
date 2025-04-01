import json
import time

FILE = "data.json"

sortTime = 0

array = [0, 2, 5, 3, 4, 1]

data = {}

def bubbleSort(array):
    global sortTime
    startTime = time.perf_counter()
    for i in range(len(array)):
            for j in range(0, len(array) - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    sortTime = time.perf_counter() - startTime
                    with open(FILE, "w") as outfile:
                        json.dump(array, outfile)
                        json.dump(sortTime, outfile)

bubbleSort(array)