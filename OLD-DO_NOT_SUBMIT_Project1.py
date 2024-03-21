# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 13:35:59 2024

@author: Shawn
"""
import numpy as np
import time

def sum(n, arr):
    begin = time.time()
    result = 0;
    for i in range(n):
        result = result + arr[i];
    time.sleep(1)
    end = time.time()
    print(f"Total runtime of the algorithm is {end - begin}")
    return result

arr = np.random.randint(100, size=(20)) 

print(sum(10,arr))


mat = np.random.randint(2, size=(5, 5)) 
mat2 = np.random.randint(2, size=(5, 5))

def scalarmatmult(n, a, b, c):
    begin = time.time()
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] * b;

    time.sleep(1)
    end = time.time()
    print(f"Total runtime of the algorithm is {end - begin}")

scalarmatmult(5, mat, 3, mat2)

print(mat2)

mat3 = np.random.randint(2, size=(5, 5))

def matrixmult (n, a, b, c):
    begin = time.time()
    for i in range(n):
        for j in range(n):
            c[i][j] = 0;
            for k in range(n):
                c[i][j] = c[i][j] + a[i][k] * b[k][j]         
    time.sleep(1)
    end = time.time()
    print(f"Total runtime of the algortihm is {end - begin}")

matrixmult(5,mat,mat2,mat3)

print(mat3)
