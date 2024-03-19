##Project 2
## 2/22/24
import random
import time

def merge(arr, temp, from_index, mid, to_index, operation_counter):
    k = from_index
    i = from_index
    j = mid + 1
    while i <= mid and j <= to_index:
        operation_counter['comparisons'] += 1  # Counting comparisons
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j <= to_index:
        temp[k] = arr[j]
        j += 1
        k += 1
    for i in range(from_index, to_index + 1):
        arr[i] = temp[i]

def merge_sort(arr, operation_counter):
    current_size = 1
    while current_size < len(arr) - 1:
        left_start = 0
        while left_start < len(arr)-1:
            mid = min((left_start + current_size - 1), (len(arr)-1))
            right_end = min((left_start + 2 * current_size - 1), (len(arr)-1))
            merge(arr, [0] * len(arr), left_start, mid, right_end, operation_counter)
            left_start += current_size * 2
        current_size *= 2

# Example usage with timing and operation counting:
operation_counter = {'comparisons': 0}
arr = [random.randint(1,10) for i in range(10000)]
start_time = time.time()
merge_sort(arr, operation_counter)
end_time = time.time()
print("Size of the array: ",arr.__sizeof__())
print(f"Merge Sort took {end_time - start_time:.6f} seconds to sort the array.")
print(f"Merge Sort made {operation_counter['comparisons']} comparisons.")


