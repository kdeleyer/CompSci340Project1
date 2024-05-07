#node
class Node:
    def __init__(self, level,profit,weight):
        self.level = level
        self.profit = profit
        self.weight = weight


#knapsack
def bound(u,W,w,n,p):
    if u.weight > W:
        return 0
    else:
        result = u.profit
        j = u.level + 1
        totweight = u.weight
        while j <= n and totweight +w[j] <= W:
            totweight += w[j]
            result = result + p[j]
            j+=1
        k = j
        if k<=n:
            result = result + (W-totweight) * (p[k]/w[k])
        return result


def knapsack2(n,p,w,W):
    #set null
    Q = []
    #new node
    v = Node(0,0,0)
    #new node
    u = Node(0,0,0)
    #set max
    maxprofit = 0
    #enqueue
    Q.append(v)
    while len(Q)!=0:
        #deque
        Q.remove(v)
        #set u
        u.level = v.level + 1
        u.weight = v.weight + w[u.level]
        u.profit = v.profit + p[u.level]

        if u.weight <= W and u.profit > maxprofit:
            maxprofit = u.profit
        if bound(u) > maxprofit:
            Q.append(u,W,w,n,p)

