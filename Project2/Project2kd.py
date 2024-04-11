##Project 2
## 2/22/24
import random
import time
## A divid and conquor algorthim that will simplify the problem
## sort the simple comparisons and add them back in order
## Merge: sorts the sub arrays then combines them
def merge(filearr, temp, from_index, mid, to_index, operation_counter):
    k = from_index
    i = from_index
    j = mid + 1
    while i <= mid and j <= to_index:
        #operation_counter['comparisons'] += 1  # Counting comparisons
        if filearr[i] <= filearr[j]:
            temp[k] = filearr[i]
            i += 1
            #operation_counter['comparisons'] += 1
        else:
            temp[k] = filearr[j]
            #operation_counter['comparisons'] += 1
            j += 1
            #operation_counter['comparisons'] += 1
        k += 1
        #operation_counter['comparisons'] += 1
    while i <= mid:
        temp[k] = filearr[i]
        #operation_counter['comparisons'] += 1
        i += 1
        #operation_counter['comparisons'] += 1
        k += 1
        #operation_counter['comparisons'] += 1
    while j <= to_index:
        temp[k] = filearr[j]
        j += 1
        #operation_counter['comparisons'] += 1
        k += 1
        #operation_counter['comparisons'] += 1
    for i in range(from_index, to_index + 1):
        filearr[i] = temp[i]
        #operation_counter['comparisons'] += 1
## divids the array into smaller sub arrays until 1 element in every array
## applies merge recursively
## O(n log n) - n is # of elements

def merge_sort(filearr, operation_counter):
    current_size = 1
    #operation_counter['comparisons'] += 1
    while current_size < len(filearr) - 1: ## while loop as long as current size is less then array size, controls processing of sub arrays
        left_start = 0
        #operation_counter['comparisons'] += 1
        while left_start < len(filearr)-1: ## while loop to continue to make subsets
            mid = min((left_start + current_size - 1), (len(filearr)-1)) ## calc mid point
            #operation_counter['comparisons'] += 1
            right_end = min((left_start + 2 * current_size - 1), (len(filearr)-1)) ## right end
            #operation_counter['comparisons'] += 1
            merge(filearr, [0] * len(filearr), left_start, mid, right_end, operation_counter)
            left_start += current_size * 2 ## moves left start to the right
            #operation_counter['comparisons'] += 1
        current_size *= 2
        #operation_counter['comparisons'] += 1

operation_counter = {'comparisons': 0}
#file list
files = ["inorder5k.txt", "inorder10k.txt", "inorder100k.txt", "random5k.txt", "random10k.txt",
         "random100k.txt", "rev5k.txt", "rev10k.txt", "rev100k.txt"]
for file in files:
    filearr = []
    with open(file) as file:
        for fline in file:
            filearr.append(int(fline.strip()))
    start_time = time.time()
    merge_sort(filearr, operation_counter)
    end_time = time.time()
    print("Size of the array: ", len(filearr))
    time_taken = (end_time - start_time) * 1000
    print(f"Merge Sort took {time_taken} milliseconds to sort the file", file.name)
    #print(f"Merge Sort made {operation_counter['comparisons']} comparisons running", file.name)


