def knapsack(i, profit, weight, items, capacity, include, best_set, num_best, max_profit, nodes_visited):
    nodes_visited[0] += 1  # Increment node count
    if weight <= capacity and profit > max_profit[0]:
        max_profit[0] = profit
        best_set[:] = include[:]
        num_best[0] = i

    if promising(i, weight, profit, items, capacity, max_profit[0]):
        include[i + 1] = 1  # Include the next item
        knapsack(i + 1, profit + items[i + 1][0], weight + items[i + 1][1], items, capacity, include, best_set, num_best, max_profit, nodes_visited)
        include[i + 1] = 0  # Exclude the next item
        knapsack(i + 1, profit, weight, items, capacity, include, best_set, num_best, max_profit, nodes_visited)

def promising(i, weight, profit, items, capacity, max_profit):
    if weight >= capacity:
        return False
    else:
        j = i + 1
        bound = profit
        totweight = weight
        while j < len(items) and totweight + items[j][1] <= capacity:
            totweight += items[j][1]
            bound += items[j][0]
            j += 1
        if j < len(items):
            bound += (capacity - totweight) * (items[j][0] / items[j][1])
        return bound > max_profit

# Initialize items with one of your test sets, e.g., Set 1 (W = 16)
items = [
    (40, 2),  # Item 1 with profit 40 and weight 2
    (30, 5),  # Item 2 with profit 30 and weight 5
    (50, 10), # Item 3 with profit 50 and weight 10
    (10, 5)   # Item 4 with profit 10 and weight 5
]

# Set the capacity of the knapsack
capacity = 16

# Arrays to track included items and best found solution
include = [0] * len(items)
best_set = [0] * len(items)
num_best = [0]
max_profit = [0]
nodes_visited = [0]

# Run the knapsack algorithm
knapsack(-1, 0, 0, items, capacity, include, best_set, num_best, max_profit, nodes_visited)

# Output the results
print("Max profit:", max_profit[0])
print("Best set:", [i+1 for i in range(len(best_set)) if best_set[i] == 1])  # Adjusted to print item numbers
print("Nodes visited:", nodes_visited[0])
