##Programer: kyle d
##date:
##Class: COMSCI 340
##Program:
import time

def sa_divide_conquer(x, y, i, j, op_count):
    op_count[0] += 1
    if i == len(x):
        return 2 * (len(y) - j), op_count
    if j == len(y):
        return 2 * (len(x) - i), op_count
    if x[i] == y[j]:
        penalty = 0
    else:
        penalty = 1

    down_right = sa_divide_conquer(x, y, i + 1, j + 1, op_count)
    right = sa_divide_conquer(x, y, i + 1, j, op_count)
    down = sa_divide_conquer(x, y, i, j + 1, op_count)
    min_cost = min(down_right[0] + penalty, right[0] + 2, down[0] + 2)

    return min_cost, op_count

# Example usage
x = "ACGTCAC"
y = "ATGTC"
start_time = time.perf_counter_ns()
result, operations = sa_divide_conquer(x, y, 0, 0, [0])
end_time = time.perf_counter_ns()
print(f"Cost: {result}, Operations: {operations[0]}, Time: {end_time - start_time} nanoseconds")
