from heapq import *
from helper import *
def ucs(graph, weights, start, end):
    visited = set()
    unexplored = [] # heap
    heappush(unexplored, [0, start])
    parents = {}
    node = None
    while len(unexplored) != 0 and node != end:
        [weight, node] = heappop(unexplored)
        if node in visited:
            continue
        visited.add(node)
        print(node)
        childs =  list(set(possible_moves(graph, weights[node], node)) - visited)
        #childs = possible_moves(graph, weights[node], node)
        for child in childs:
            if child not in parents.keys() or weight + weights[node] < weights[parents[child]]:
                parents[child] = node
            heappush(unexplored, [weights[node] + weight, child])
    return get_path(parents, start, end)

