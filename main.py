import random
import numpy as np
from random import randrange
from scipy.spatial import distance_matrix

cities_cordinates = [[4,3],[2,4],[9,3],[7,2],[1,6],[3,11]]


def generateGnomes(genNumber):
    tempTable = []
    gnomTable = []
    for i in range(0,genNumber):
        tempGnom = randomGnom(len(cities_cordinates))
        tempGnom.append(distanceMatrix(tempGnom))
        gnomTable.append(tempGnom)
    #print(*tempTable, sep='\n')
    return gnomTable

def randomGnom(arrLength):
    gnomCodes = []
    for i in range(1,arrLength):
        gnomNum = random.choice([x for x in range(arrLength) if x not in gnomCodes and x > 0])
        gnomCodes.append(gnomNum)
    gnomCodes.insert(arrLength,0)
    return gnomCodes

def distanceMatrix(gnomArr):
    matrix=distance_matrix(cities_cordinates,cities_cordinates)
    calcLength = 0
    for i in range(0,len(gnomArr)):
        calcLength += matrix[i][gnomArr[i]]
    return calcLength


def gnomeSelection(gnomeTable):
    newGnomeTable = []
    tempData1Table = []
    tempData2Table = []
    tempIndex = []

    for i in range(0,len(gnomeTable)):
        tempData1Table.append(gnomeTable[i][6])
    print(tempData1Table)
    tempData2Table = sorted(tempData1Table)[:5]
    print(tempData2Table)
    #ahol a tempdata 1 értéke egyenlőa tempdata2-vel
    for i in range(0,len(tempData2Table)):
        for x in range(0,len(tempData1Table)):
            if tempData2Table[i] == tempData1Table[x]:
                tempIndex.append(x)
    print(tempIndex)
    
    return newGnomeTable

print(*generateGnomes(10), sep='\n')
print("-----------------")
print(*gnomeSelection(generateGnomes(10)),sep='\n')
