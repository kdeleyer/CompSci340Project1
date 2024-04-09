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
        operation_counter['comparisons'] += 1  # Counting comparisons
        if filearr[i] <= filearr[j]:
            temp[k] = filearr[i]
            i += 1
        else:
            temp[k] = filearr[j]
            j += 1
        k += 1
    while i <= mid:
        temp[k] = filearr[i]
        i += 1
        k += 1
    while j <= to_index:
        temp[k] = filearr[j]
        j += 1
        k += 1
    for i in range(from_index, to_index + 1):
        filearr[i] = temp[i]
## divids the array into smaller sub arrays until 1 element in every array
## applies merge recursively
## O(n log n) - n is # of elements

def merge_sort(filearr, operation_counter):
    current_size = 1
    while current_size < len(filearr) - 1: ## while loop as long as current size is less then array size, controls processing of sub arrays
        left_start = 0
        while left_start < len(filearr)-1: ## while loop to continue to make subsets
            mid = min((left_start + current_size - 1), (len(filearr)-1)) ## calc mid point
            right_end = min((left_start + 2 * current_size - 1), (len(filearr)-1)) ## right end
            merge(filearr, [0] * len(filearr), left_start, mid, right_end, operation_counter)
            left_start += current_size * 2 ## moves left start to the right
        current_size *= 2

operation_counter = {'comparisons': 0}
start_time = time.time()

filearr = []
with open('rev5k.txt') as file:
    for fline in file:
        filearr.append(int(fline.strip()))

merge_sort(filearr, operation_counter)
end_time = time.time()
print("Size of the array: ", len(filearr))
time_taken = (end_time - start_time) * 1000
print(f"Merge Sort took {time_taken:.6f} milliseconds to sort the array.")
print(f"Merge Sort made {operation_counter['comparisons']} comparisons.")


