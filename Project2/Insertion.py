# (took 2hrs)
import time


def insertion(arr):
    #time
    start = time.time()
    # if > 1
    if(len(arr)>1):
        #new array
        arr2 = []
        #for in n
        for i in range(len(arr)):
            arr2.append(arr[i])
            #arr2 length
            track = len(arr2)-1
            #current
            current = track
            #for in arr2
            while track >= 0:
                #if greater than
                if arr2[track] > arr2[current]:
                    #swip swap
                    temp = arr2[track]
                    arr2[track] = arr2[current]
                    arr2[current] = temp
                    current-=1
                track-=1
        #time
        end = time.time()
        print("Total time ms is : ", end-start)
        return arr2







filearr = []
# open and strip
with open('../rev5k.txt') as file:
    for fline in file:
        filearr.append(int(fline.strip()))
print(insertion(filearr))
