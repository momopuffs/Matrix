from random import *
import numpy as np

class Matrix:
    '''
        Purpose: Object constructor
        Parameter: string , file name
        Return: none
    '''
    def __init__(self, filePath):
        self.file=open(filePath,'r')
        data = self.file.read()
        self.digits= data.split()

    '''           
            Purpose: Create a 10 by 10 matrix
            Parameter: none
            Return:  int 10 by 10 matrix
    '''
    def createMatrix (self):
        matrixName = [[0 for col in range(10)] for row in range(10)]

        indexDigit = 0
        for col in range(10):
            for row in range(10):
                matrixName[row][col] = int (self.digits[indexDigit])
                indexDigit += 1
        return matrixName
    '''
        Purpose: return a list of unquied random column indexes 
        Parameter: int  -- The number of columns.
        Return:  int list 
    '''
    def RandomColum(selfs,randomed):
        list=[ 0 for x in range (randomed)]
        tempList=[0 for y in range(randomed)]
        flag=0
        tempFlag=1
        while flag!=1:
            for index in range(randomed):
                list[index]= randint(1,10)-1
            tempList=sorted(list)
            print(tempList)
            for i in range (randomed-1):
                if tempList[i]==tempList[i+1]:
                    tempFlag=0
            if tempFlag==1:
                flag=1
            tempFlag=1
        return list
    '''
        Purpose: create a smaller matrix base on the columns of orginial matrix
        Parameter:int orgininal matrix, int index of columns
        Return: int maxtrix
    '''
    def createNewMatrix(selfself,orgiMatrix,numOfColums):
        #Create a small matrix
         newMatrix=[[0 for row in range (10)] for col in range(len(numOfColums))]
         listIndex=0
         while listIndex !=len(numOfColums):
            for row1 in range (10):
                 newMatrix[listIndex][row1]=orgiMatrix[numOfColums[listIndex]][row1]
            sorted(newMatrix[listIndex],reverse=True)
            listIndex+=1
         #   print(numOfColums[listIndex])
         return newMatrix
    '''
        Purpose: Object destructor
        Parameter: none
        return: none
    '''
    def _del__(self):
        self.file.close()


filePath="data.txt"
matrix= Matrix(filePath)
matrixName = [[0 for col in range(10)] for row in range(10)]
SmallMatrix = [[0 for row1 in range(10)] for col1 in range(3)]
randomNumber=3
matrixName=matrix.createMatrix()
list=matrix.RandomColum(randomNumber)
print ("Three Random columns are")
print (list)
SmallMatrix=matrix.createNewMatrix(matrixName,list)

print(SmallMatrix)
print(SmallMatrix)
