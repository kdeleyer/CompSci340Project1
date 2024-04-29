import time

class KnapsackSolver:
    def __init__(self, profits, weights, max_weight):
        self.profits = profits
        self.weights = weights
        self.max_weight = max_weight
        self.n = len(weights)
        self.max_profit = 0
        self.best_set = []
        self.include = ['no'] * self.n
        self.node_count = 0
        self.elapsed_time = 0

    def promising(self, i, profit, weight):
        if weight >= self.max_weight:
            return False
        else:
            j = i + 1
            bound = profit
            totweight = weight
            while j < self.n and totweight + self.weights[j] <= self.max_weight:
                totweight += self.weights[j]
                bound += self.profits[j]
                j += 1
            k = j
            if k < self.n:
                bound += (self.max_weight - totweight) * (self.profits[k] / self.weights[k])
            return bound > self.max_profit

    def knapsack(self, i, profit, weight):
        self.node_count += 1
        if weight <= self.max_weight and profit > self.max_profit:
            self.max_profit = profit
            self.best_set = self.include[:i]
        if self.promising(i, profit, weight):
            self.include[i] = 'yes'
            self.knapsack(i + 1, profit + self.profits[i], weight + self.weights[i])
            self.include[i] = 'no'
            self.knapsack(i + 1, profit, weight)

    def solve(self):
        start_time = time.time()
        self.knapsack(0, 0, 0)
        self.elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds
        print(f"There was a total profit of {self.max_profit}")
        selected_items = [i+1 for i, x in enumerate(self.best_set) if x == 'yes']
        print(f"The items selected were {' '.join(map(str, selected_items))}")
        print(f"Number of nodes visited was {self.node_count}")
        print(f"Time taken: {self.elapsed_time:.2f} milliseconds")  # Time in milliseconds

# usage with one set of data:
profits = [40, 30, 50, 10]
weights = [2, 5, 10, 5]
max_weight = 16

solver = KnapsackSolver(profits, weights, max_weight)
solver.solve()
