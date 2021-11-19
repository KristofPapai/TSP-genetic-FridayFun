import random
import numpy as np
from random import randrange
from scipy.spatial import distance_matrix

cities_cordinates = [[4,3],[2,4],[9,3],[7,2],[1,6],[3,11]]


def generateGnomes(genNumber):
    #distanceMatrix(randomGnom(len(cities_cordinates)))
    gnomTable = []
    for i in range(0,genNumber):
        tempGnom = randomGnom(len(cities_cordinates))
        tempGnom.append(distanceMatrix(tempGnom))
        gnomTable.append(tempGnom)
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

print(*generateGnomes(10), sep='\n')