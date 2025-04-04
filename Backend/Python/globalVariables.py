inputFile = '../../inputData.csv'
outputFile = '../../pythonData.csv'

sortTime = 0.0

array = [1, 2, 3, 4, 5]

length = 5

def createHeaders(array, outputArray):
    tempArray = []
    for i in range(len(array)):
        tempArray.append(f"A{i}")
        
    tempArray.append("Time")
    tempArray.append("Type")
    outputArray.append(tempArray)

def addDataToOutput(sortArray, outputArray, time, type):
    for i in range(len(sortArray)):
        outputArray.append(i)
    outputArray.append(time)
    outputArray.append(type)