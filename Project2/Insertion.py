# (took 2hrs)
import time


def insertion(arr):
    #op tracker
    ittrack = 0
    #time
    start = time.time()
    # if > 1
    if(len(arr)>1):
        #ittrack+=1
        #new array
        arr2 = []
        #ittrack+=1
        #for in n
        for i in range(len(arr)):
            #ittrack+=1
            arr2.append(arr[i])
            #ittrack+=1
            #arr2 length
            track = len(arr2)-1
            #ittrack+=1
            #current
            current = track
            #ittrack+=1
            #for in arr2
            while track >= 0:
                #ittrack+=1
                #if greater than
                if arr2[track] > arr2[current]:
                    #ittrack+=1
                    #swip swap
                    temp = arr2[track]
                    #ittrack+=1
                    arr2[track] = arr2[current]
                    #ittrack+=1
                    arr2[current] = temp
                    #ittrack+=1
                    current-=1
                    #ittrack+=1
                track-=1
                #ittrack+=1
        #time
        end = time.time()
        print("Total time ms is : ", end-start)
        #print("The total operations are: " , ittrack)
        return arr2







filearr = []
# open and strip
with open('../rev5k.txt') as file:
    for fline in file:
        filearr.append(int(fline.strip()))
print(insertion(filearr))
