##Programer: kyle d
##date:
##Class: math.225
##Program:

import time
def as_dynamic(x, y):
    m, n = len(x), len(y)
    cost = [[0] * (n + 1) for _ in range(m + 1)]
    op_count = 0

    # Initialize the cost of aligning with empty subsequences
    for i in range(1, m + 1):
        cost[i][0] = i * 2
        op_count += 1
    for j in range(1, n + 1):
        cost[0][j] = j * 2
        op_count += 1

    # Fill the cost matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            op_count += 1
            if x[i - 1] == y[j - 1]:
                penalty = 0
            else:
                penalty = 1
            cost[i][j] = min(cost[i - 1][j - 1] + penalty,
                             cost[i - 1][j] + 2,
                             cost[i][j - 1] + 2)

    return cost[m][n], op_count

# Example usage
x = "ACGTCAC"
y = "ATGTC"
start_time = time.perf_counter_ns()
cost, operations = as_dynamic(x, y)
end_time = time.perf_counter_ns()
print(f"Cost: {cost}, Operations: {operations}, Time: {end_time - start_time} nanoseconds")

