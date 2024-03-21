# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 15:15:54 2024

@author: Shawn Fahy
"""
import time
import numpy as np

#sum of the array added together
def sum(n, array):
    #result
    result = 0;
    #ns start time
    begin = time.time_ns()
    #for i less than n
    for i in range(n):
        result = result + array[i]
    #end   
    end = time.time_ns()
    #print runtime
    return (int)(end-begin)

#algorithm 2
def scalarmatmult(n, a, b, c):
    #ns start time
    begin = time.time_ns()
    #for
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] * b

    #end time
    end = time.time_ns()
    #print runtime
    return (int)(end-begin)

#algo 3
#product of two matrixes
def matrixmult(n, a, b, c):
    #begin time
    begin = time.time_ns()
    for i in range(n):
        for j in range(n):
            c[i][j] = 0;
            for k in range(n):
                 c[i][j] = c[i][j] + a[i][k] * b[k][j]
    #end time
    end = time.time_ns()
    return (int)(end-begin)

#matrix creator
def createMatrix(a, b):
    matrix = np.random.randint(2,size=(a,b))
    return matrix

#array creator
def createArray(a):
    array = np.random.randint(10, size=(a))
    return array

#total runtimes
def printTot():
    #for methods
    for i in range(3):
        #for size
        for j in range(7):
            #sum to print
            total = (tracker[0][j][i]+tracker[1][j][i]+tracker[2][j][i]+tracker[3][j][i]+tracker[4][j][i]+tracker[5][j][i]+tracker[6][j][i])/7;
            #print runtime
            print("The runtime of algorithm " + str((i+1)) + " in nanoseconds for size " + str(auto[j]) + " is ", (int)(total))

auto = [10, 50, 100, 500, 1000, 2500, 5000]
#tracker for runtime
tracker = [[ [0 for col in range(3)] for col in range(7)] for row in range(7)]
#five runs
for j in range(7):
  #track runs in inner loop
  t = 0
  for i in auto:
     #test runs
     #Array size
     print("Working on array size of: " + str(i))
     #test 1
     array = createArray(i)
     tracker[j][t][0] = sum(i, array)

     #test2
     matrix1 = createMatrix(i, i)
     matrix2 = createMatrix(i, i)
     tracker[j][t][1] = scalarmatmult(i, matrix1, i, matrix2)

     #test 3
     matrix3 = createMatrix(i, i)
     tracker[j][t][2] = matrixmult(i, matrix1, matrix2, matrix3)

     #add t
     t = t + 1
#totals
printTot()