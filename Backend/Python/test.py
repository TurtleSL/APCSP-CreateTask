import csv
import time

FILE = "pythonData.csv"

sortTime = 0

array = [0, 2, 5, 3, 4, 1]

data = []

with open(FILE, mode='w', newline='') as file:
    writer = csv.writer(file)

    array_str = str(array)
    
    writer.writerow(array_str, 0.02)

# def bubbleSort(array):
#     global sortTime
#     startTime = time.perf_counter()
#     for i in range(len(array)):
#             for j in range(0, len(array) - i - 1):
#                 if array[j] > array[j + 1]:
#                     array[j], array[j + 1] = array[j + 1], array[j]
#                     sortTime = time.perf_counter() - startTime
#                     data.update(array : sortTime)
#                     print(data)

#bubbleSort(array)