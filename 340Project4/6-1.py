#node
import time
global nodevisted
global operations
nodevisted = 0
operations = 0


class Node:
    def __init__(self, level,profit,weight):
        self.level = level
        self.profit = profit
        self.weight = weight


#knapsack
def bound(u,W,w,n,p):
    global operations
    if u.weight > W:
        operations+=1
        return 0
    else:
        result = u.profit
        j = u.level
        totweight = u.weight
        while j <= n and totweight + w[j] <= W:
            totweight += w[j]
            result = result + p[j]
            j+=1
        k = j
        if k<=n:
            operations+=1
            result = result + (W-totweight) * (p[k]/w[k])
        return result


def knapsack2(n,p,w,W):
    #set null
    global nodevisted
    global operations
    Q = []
    T = []
    #new node
    v = Node(0,0,0)
    #new node
    u = Node(0,0,0)
    #set max
    maxprofit = 0
    #enqueue
    Q.append(v)
    while len(Q)!=0:
        nodevisted+=1
        #deque
        v = Q.pop(0)
        #set u
        u.level = v.level + 1
        u.weight = v.weight + w[u.level]
        u.profit = v.profit + p[u.level]
        if u.weight <= W and u.profit > maxprofit:
            operations+=1
            maxprofit = u.profit
        if bound(u,W,w,n,p) > maxprofit:
            operations+=1
            Q.append(u)
            T.append(u.weight)
    return(maxprofit,T)


# Define items [(profit, weight), ...] based on Set 4
items = [40,30,50,10]
items2 = [2,5,10,5]

# Total number of items and knapsack capacity from Set 4
n = len(items)
W = 16
start = time.time_ns()
print("Profit, and Weights of Solution:",knapsack2(n, items,items2, W))
end = time.time_ns()
print("Execution time in nanoseconds: ",(end-start))
print("Number of nodes visted:",nodevisted)
print("operations:",operations)