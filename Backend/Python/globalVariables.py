inputFile = '../../inputData.csv'
outputFile = '../../pythonData.csv'

sortTime = 0.0

length = 5

def createHeaders(array, outputArray):
    tempArray = []
    for i in range(len(array)):
        tempArray.append(f"A{i}")
        
    tempArray.append("Time")
    tempArray.append("Type")
    outputArray.append(tempArray)

def addDataToOutput(sortArray, time, type, outputArray):
    temp = []
    for i in range(len(sortArray)):
        temp.append(sortArray[i])
    temp.append(time)
    temp.append(type)
    outputArray.append(temp)