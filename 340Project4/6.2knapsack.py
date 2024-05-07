import heapq

class Node:
    def __init__(self, level=None, profit=0, weight=0, bound=0):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = bound

    def __lt__(self, other):
        return self.bound > other.bound  # Max-heap based on bound

def bound(node, n, W, items):
    if node.weight >= W:
        return 0
    else:
        result = node.profit
        totweight = node.weight
        j = node.level + 1
        while j < n and totweight + items[j][1] <= W:
            totweight += items[j][1]
            result += items[j][0]
            j += 1
        if j < n:
            result += (W - totweight) * (items[j][0] / items[j][1])
        return result

def knapsack(n, items, W):
    PQ = []
    max_profit = 0
    nodes_visited = 0

    v = Node(-1, 0, 0)  # Starting node
    v.bound = bound(v, n, W, items)
    heapq.heappush(PQ, v)

    while PQ:
        v = heapq.heappop(PQ)
        nodes_visited += 1
        if v.bound > max_profit:
            u = Node(v.level + 1, v.profit + items[v.level + 1][0], v.weight + items[v.level + 1][1])
            if u.weight <= W and u.profit > max_profit:
                max_profit = u.profit
            u.bound = bound(u, n, W, items)
            if u.bound > max_profit:
                heapq.heappush(PQ, u)

            u = Node(v.level + 1, v.profit, v.weight)
            u.bound = bound(u, n, W, items)
            if u.bound > max_profit:
                heapq.heappush(PQ, u)

    return max_profit, nodes_visited

# Define items [(profit, weight), ...] based on Set 4
items = [
    (50, 2),
    (55, 10),
    (15, 5),
    (50, 20)
]

# Total number of items and knapsack capacity from Set 4
n = len(items)
W = 40

max_profit, nodes_visited = knapsack(n, items, W)
print(f"Max profit: {max_profit}")
print(f"Nodes visited: {nodes_visited}")
