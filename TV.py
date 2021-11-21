import csv
import numpy

def getDataSource(dataPath):
    list1 = []
    list2 = []

    with open(dataPath) as file:
        reader = csv.DictReader(file)

        for i in reader:
            list1.append(float(i["Size of TV"]))
            list2.append(float(i["Average time"]))

    return {'x': list1, 'y': list2}

def findCorrelation(dataSource):
    corr = numpy.corrcoef(dataSource['x'], dataSource['y'])
    print("The Correlation Is: ", corr[0,1])

def setup():
    dataPath = "TV.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)

setup()