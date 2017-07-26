from heapq import *
from helper import *
def ucs(graph, weights, start, end):
    visited = set()
    unexplored = [] # heap
    heappush(unexplored, [weights[start], start])
    parents = {}
    node = None
    while len(unexplored) != 0 and node != end:
        [weight, node] = heappop(unexplored)
        if node in visited:
            continue
        visited.add(node)
        childs = possible_moves(graph, weights[node], node)
        for child in childs:
            if child not in parents.keys() or weight < weights[parents[child]]:
                parents[child] = node
            heappush(unexplored, [weights[child] + weight, child])
    return get_path(parents, start, end)
