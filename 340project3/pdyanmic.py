#Written by PennP on 5/1/24
#time

import time
# #global vars
y1 = ['A','A','C','A','G','T','T','A','C','C']
x1 = ['T','A','A','G','G','T','C','A',]
#set2
x2 = ['C', 'C', 'G', 'G', 'G', 'T', 'T', 'A', 'C', 'C', 'A']
y2 = ['G', 'G', 'A', 'G', 'T', 'T', 'C', 'A']
#set
x3 = ['A', 'A', 'C', 'A', 'G', 'T', 'T', 'A', 'C', 'C', 'T', 'A']
y3 = ['T', 'A', 'A', 'G', 'G', 'T', 'C', 'A', 'G', 'C']


operation = 0
def dynamic(x,y,xarr,yarr):
    start = time.perf_counter_ns()
    operation = 0
    #create array
    temp = fillarr(x,y,xarr,yarr)
    trav = temp[0]
    operation+=temp[1]
    #until solved
    x1 = 0
    y1 = 0
    while x1 != x and y != y:
        #print(x1,y1)
        operation+=1
        currentval = trav[y1][x1]
        #test down
        if trav[y1+1][x1]+2 == currentval:
            operation+=1
            y1= y1+1
        #test left
        elif trav[y1][x1+1]+2 == currentval:
            operation+=1
            x1= x1+1
        #else no other option
        else:
            operation+=1
            y1+=1
            operation+=1
            x1+=1
    end = time.perf_counter_ns()
    returntime = end - start
    return [returntime,operation]




def fillarr(x,y,arrx,arry):
    operation = 0
    #2d array
    operation +=1
    final = [[0 for _ in range(x+1)] for _ in range(y+1)]
    #perform fill opp from right to left
    for j in range(len(final[1])):
        #fill arr
        operation+=1
        final[y][j] = 2*(x-j)
    #fill y
    for i in range(len(final)):
        operation+=1
        final[i][x] = 2*(y-i)
    #calc all
    #y arr
    #fill the rest of the array diagonally
    # i am going to lose it why do you have to use range like this
    for i in range(y-1, -1, -1):
        for j in range(x-1, -1, -1):
            #if math and diag then no penalty
            if arrx[j] == arry[i]:
                #no penatly
                operation+=1
                final[i][j] = final[i+1][j+1]
            else:
                #algo from book
                operation+=1
                final[i][j] = min(final[i+1][j+1] + 1, final[i+1][j] + 2, final[i][j+1] + 2)
    #return completed array to use in the actual algorithm
    return [final,operation]


#automated runtime
for i in range(1,4):
    print("Running size",i,"...")
    if i == 1:
        temp = dynamic(len(x1),len(y1),x1,y1)
    elif i == 2:
        temp = dynamic(len(x2),len(y2),x2,y2)
    else:
        temp = dynamic(len(x3),len(y3),x3,y3)
    print("Time taken in nanoseconds is:",temp[0],"Operations:",temp[1])
