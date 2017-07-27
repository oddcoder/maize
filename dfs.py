from helper import *
def dfs(graph, weights, start, end):
    visited = set()
    unexplored = [start]
    parents = {}
    node = None
    while len(unexplored) != 0 and node != end:
        node = unexplored.pop()
        if node in visited:
            continue
        visited.add(node)
        childs =  list(set(possible_moves(graph, weights[node], node)) - visited)
        for child in childs:
            parents[child] = node
            unexplored.append(child)
    import pdb
    pdb.set_trace()
    return get_path(parents, start, end)
