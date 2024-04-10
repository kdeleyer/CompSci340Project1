"""
@author: Penn Potter
"""
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
        return(end-start)





filearr = []
#file list
files = ["../inorder5k.txt", "../inorder10k.txt", "../inorder100k.txt", "../random5k.txt", "../random10k.txt",
         "../random100k.txt", "../rev5k.txt", "../rev10k.txt", "../rev100k.txt"]
for file in files:
    # open and strip
    with open(file) as file:
        for fline in file:
            filearr.append(int(fline.strip()))
    print("The time taken for", file.name, "is", insertion(filearr),"ms")
