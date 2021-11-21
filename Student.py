import csv
import numpy

def getDataSource(dataPath):
    list1 = []
    list2 = []

    with open(dataPath) as file:
        reader = csv.DictReader(file)

        for i in reader:
            list1.append(float(i["Marks In Percentage"]))
            list2.append(float(i["Days Present"]))

    return {'x': list1, 'y': list2}

def findCorrelation(dataSource):
    corr = numpy.corrcoef(dataSource['x'], dataSource['y'])
    print("The Correlation Is: ", corr[0,1])

def setup():
    dataPath = "Student.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)

setup()