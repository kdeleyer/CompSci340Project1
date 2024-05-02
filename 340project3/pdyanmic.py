#Written by PennP on 5/1/24

#global vars
y1 = ['A','A','C','A','G','T','T','A','C','C']
x1 = ['T','A','A','G','G','T','C','A']


def dynamic(x,y,xarr,yarr):
    #create array
    trav = fillarr(x,y,xarr,yarr)
    #until solved
    x1 = x
    y1 = y
    #total
    total = 0
    while x1 != 0 and y1 != 0:
        print(x1,y1)
        #if bigger
        total = trav[y1][x1]
        if trav[y1-1][x1-1] < trav[y1-1][x1] and trav[y1-1][x1-1] < trav[y1][x1-1]:
            x1 = x1-1
            y1 = y1-1
        elif trav[y1-1][x1] < (trav[x1-1][y1-1] and trav[y1][x1-1]):
            y1 = y1-1
        else:
            x1 = x1-1
    total = trav[0][0]
    return total




def fillarr(x,y,arrx,arry):
    #2d array
    final = [[0 for _ in range(x+1)] for _ in range(y+1)]
    #perform fill opp from right to left
    for j in range(len(final[1])):
        #fill arr
        final[y][j] = 2*(x-j)
    #fill y
    for i in range(len(final)):
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
                final[i][j] = final[i+1][j+1]
            else:
                #algo from book
                final[i][j] = min(final[i+1][j+1] + 1, final[i+1][j] + 2, final[i][j+1] + 2)
    #return completed array to use in the actual algorithm
    return final


print(dynamic(len(x1),len(y1),x1,y1))

