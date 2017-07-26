from helper import *
def bfs(graph, weights, start, end):
    visited = set()
    unexplored = [start] # queue
    parents = {}
    node = None
    while len(unexplored) != 0 or node == end:
        node = unexplored.pop(0)
        if node in visited:
            continue
        visited.add(node)
        childs =  possible_moves(graph, weights[node], node)
        for child in childs:
            if child not in parents.keys():
                parents[child] = node
        unexplored += childs
    return get_path(parents, start, end)
