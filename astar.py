from heapq import *
from helper import *
from  math import *

def eucliedean(current, dest): 
    (x1, y1) = current
    (x2, y2) = dest
    return sqrt((y2 - y2 )**2 + (x2- x1)**2)

def manhattan(current, dest):
    (x1, y1) = current
    (x2, y2) = dest
    return abs(x1 - x2) + abs(y1 - y2)


def astar(graph, weights, start, end, heuristic):
    visited = set()
    unexplored = [] # heap
    heappush(unexplored, [1 + heuristic(start, end), start])
    parents = {}
    node = None
    #while there are unexplored frontier nodes and we haven't found the end yet
    while len(unexplored) != 0 and node != end:
    #weight takes heurestic cost value and node takes coordinates of node having this weight
        [weight, node] = heappop(unexplored)
        if node in visited:
            continue #pop another node
        visited.add(node)
        print(node)
        childs =  list(set(possible_moves(graph, weights[node], node)) - visited)
        #childs = possible_moves(graph, weights[node], node)
        for child in childs:
            #check if any of the children is visited before,
#and heuristic of current node + weight of child + heuristic of child -heurisitic of parent < steps of parent of the child
            if child not in parents.keys() or weight < weights[parents[child]]:
                parents[child] = node
            heappush(unexplored, [weights[child] + weight + heuristic(child, end) - heuristic(node, end), child])
    return get_path(parents, start, end)

